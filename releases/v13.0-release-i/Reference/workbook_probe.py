"""Scoped interpreter of delivered input/contribution/reconciliation formulas.

Not Excel/LibreOffice parity. It evaluates a named formula subset from the XLSX,
uses retained caches for other unmodified dependencies, and independently checks
snapshot equality and formula presence. Unsupported syntax fails explicitly.
"""
from __future__ import annotations
from copy import deepcopy
from functools import lru_cache
from pathlib import Path
import math,re,json
from Workbook_Verifier import inspect

class ProbeError(ValueError):pass
class Unsupported(RuntimeError):pass
TOKEN=re.compile(r'\s*(?:("(?:[^"]|"")*")|(\'(?:[^\']|\'\')*\')|((?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)|([A-Za-z_$][A-Za-z0-9_.$]*)|(<=|>=|<>|[=<>+*/^&:,()!-]))')
def tokenize(s):
 out=[];i=0
 while i<len(s):
  m=TOKEN.match(s,i)
  if not m:raise Unsupported('Formula syntax: '+s[i:i+60])
  out.append(next(g for g in m.groups()if g is not None));i=m.end()
 return out
class Parser:
 def __init__(self,s):self.t=tokenize(s);self.i=0
 def peek(self):return self.t[self.i] if self.i<len(self.t) else None
 def pop(self):x=self.peek();self.i+=1;return x
 def expect(self,x):
  if self.pop()!=x:raise Unsupported('Expected '+x)
 def expr(self,minp=0):
  t=self.pop()
  if t in ('+','-'):left=('unary',t,self.expr(50))
  elif t=='(':left=self.expr();self.expect(')')
  elif t is None:raise Unsupported('Unexpected end')
  elif t.startswith('"'):left=('value',t[1:-1].replace('""','"'))
  elif re.fullmatch(r'(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?',t):left=('value',float(t))
  elif self.peek()=='(':
   self.pop();args=[]
   if self.peek()!=')':
    while True:
     args.append(self.expr())
     if self.peek()!=',':break
     self.pop()
   self.expect(')');left=('call',t.upper().replace('_XLFN.',''),args)
  elif t.upper() in ('TRUE','FALSE'):left=('value',t.upper()=='TRUE')
  else:
   sn=None;ref=t
   if self.peek()=='!':self.pop();sn=t.strip("'").replace("''", "'");ref=self.pop()
   end=ref
   if self.peek()==':':self.pop();end=self.pop()
   left=('ref',sn,ref.replace('$',''),end.replace('$',''))
  prec={'=':10,'<>':10,'<':10,'>':10,'<=':10,'>=':10,'&':15,'+':20,'-':20,'*':30,'/':30,'^':40}
  while self.peek() in prec and prec[self.peek()]>=minp:
   op=self.pop();right=self.expr(prec[op]+(0 if op=='^' else 1));left=('op',op,left,right)
  return left
@lru_cache(maxsize=32768)
def parse(s):
 p=Parser(s);a=p.expr()
 if p.peek() is not None:raise Unsupported('Unconsumed formula tokens')
 return a

def isnum(x):return type(x) in (int,float) and math.isfinite(x)
def num(x):
 if x is None:return 0.
 if isnum(x):return float(x)
 if isinstance(x,bool):return int(x)
 raise ProbeError('Numeric value required')
def flatten(xs):
 for x in xs:
  if isinstance(x,list):yield from flatten(x)
  else:yield x
def colno(c):
 n=0
 for x in c:n=n*26+ord(x)-64
 return n
def colname(n):
 s=''
 while n:n,k=divmod(n-1,26);s=chr(65+k)+s
 return s
class WorkbookProbe:
 def __init__(self,data):self.data=deepcopy(data);self.memo={};self.active=set();self.frozen_dependencies=set()
 def set(self,s,c,value=None,formula=None):
  old=self.data['cells'][s].get(c,{});self.data['cells'][s][c]={**old,'value':value,'formula':formula};self.memo.clear()
 def refvalue(self,s,c):return self.data['cells'].get(s,{}).get(c,{}).get('value')
 def refs(self,s,a,b):
  def bits(x):
   m=re.fullmatch('([A-Z]+)([0-9]*)',x)
   if not m:raise Unsupported('Reference '+x)
   return colno(m[1]),int(m[2]) if m[2] else None
  c1,r1=bits(a);c2,r2=bits(b)
  if r1 is None or r2 is None:
   maxrow=max((int(re.search('[0-9]+',c).group())for c in self.data['cells'][s]),default=1);r1=1;r2=maxrow
  return [(s,colname(c)+str(r))for r in range(r1,r2+1)for c in range(c1,c2+1)]
 def get(self,s,c):
  key=(s,c)
  if key in self.memo:return self.memo[key]
  if key in self.active:raise ProbeError('Circular dependency '+s+'!'+c)
  self.active.add(key)
  try:
   e=self.data['cells'].get(s,{}).get(c,{});f=e.get('formula')
   if s=='Build_Integrity' and c=='B5':v=self.snapshot_mismatches()
   elif s=='Build_Integrity' and c=='B6':v=self.presence_mismatches()
   elif f is None:v=e.get('value')
   elif s in ('Impact_Input','I_prop','Contribution_Analysis','Build_Integrity','Sanity_Checklist') or (s=='Release_Lint' and c in ('C5','C6')) or (s=='Parameters' and c=='B42') or (s=='RLS' and c in ('C5','C32')) or (s=='NCRC' and c=='A5'):
    v=self.eval(parse(f),s)
   else:
    self.frozen_dependencies.add(s+'!'+c);v=e.get('value')
   self.memo[key]=v;return v
  finally:self.active.remove(key)
 def snapshot_mismatches(self):
  d=self.data['cells']['Build_Snapshot'];n=0
  for a,e in d.items():
   if not re.fullmatch('CL[0-9]+',a) or a=='CL1':continue
   r=a[2:];s=e['value'];c=d.get('CM'+r,{}).get('value');expected=d.get('CN'+r,{}).get('value')
   if not isinstance(s,str) or not isinstance(c,str):continue
   if not isinstance(s,str) or not isinstance(c,str):continue
   actual=self.get(s,c)
   if isnum(actual)and isnum(expected):match=actual==expected
   else:match=type(actual)==type(expected)and actual==expected
   n+=not match
  return n
 def presence_mismatches(self):
  d=self.data['cells']['Workbook_Formula_Guard'];n=0
  for a,e in d.items():
   if not re.fullmatch('D[0-9]+',a)or not e.get('formula'):continue
   r=a[1:];s=d['A'+r]['value'];c=d['B'+r]['value'];n+=self.data['cells'][s].get(c,{}).get('formula') is None
  return n
 def eval(self,a,s):
  typ=a[0]
  if typ=='value':return a[1]
  if typ=='ref':
   refs=self.refs(a[1]or s,a[2],a[3]);v=[self.get(*r) for r in refs];return v[0]if len(v)==1 else v
  if typ=='unary':return num(self.eval(a[2],s))*(1 if a[1]=='+'else-1)
  if typ=='op':
   op=a[1];l=self.eval(a[2],s);r=self.eval(a[3],s)
   if op=='&':return str(l or '')+str(r or '')
   if op in ('=','<>'):
    eq=l.upper()==r.upper()if isinstance(l,str)and isinstance(r,str)else l==r
    return eq if op=='='else not eq
   if op in ('<','>','<=','>='):
    l,r=num(l),num(r);return {'<':l<r,'>':l>r,'<=':l<=r,'>=':l>=r}[op]
   l,r=num(l),num(r)
   if op=='+':return l+r
   if op=='-':return l-r
   if op=='*':return l*r
   if op=='/':
    if r==0:raise ProbeError('Division by zero')
    return l/r
   if op=='^':return l**r
  if typ!='call':raise Unsupported(str(a))
  f,args=a[1],a[2]
  if f=='IF':return self.eval(args[1]if self.eval(args[0],s)else args[2],s)
  if f=='IFERROR':
   try:return self.eval(args[0],s)
   except (ProbeError,ZeroDivisionError,ValueError):return self.eval(args[1],s)
  if f in ('ISNUMBER','ISBLANK','ISFORMULA'):
   if f=='ISNUMBER':return isnum(self.eval(args[0],s))
   ar=args[0]
   if ar[0]!='ref':raise Unsupported(f+' requires reference')
   refs=self.refs(ar[1]or s,ar[2],ar[3]);e=self.data['cells'][refs[0][0]].get(refs[0][1],{})
   return e.get('formula')is not None if f=='ISFORMULA'else e.get('formula')is None and e.get('value')is None
  vs=[self.eval(x,s)for x in args];flat=list(flatten(vs))
  if f=='AND':return all(flat)
  if f=='OR':return any(flat)
  if f=='COUNT':return sum(isnum(x)for x in flat)
  if f=='COUNTA':
   # Formula results, including an empty string, are occupied cells.
   total=0
   for ar,v in zip(args,vs):
    if ar[0]=='ref':
     for sn,cell in self.refs(ar[1]or s,ar[2],ar[3]):
      e=self.data['cells'][sn].get(cell,{});total+=e.get('formula')is not None or e.get('value')is not None
    else:total+=v is not None
   return total
  if f=='SUM':return sum(x for x in flat if isnum(x))
  if f=='ROUND':return round(num(vs[0]),int(num(vs[1])))
  if f=='ABS':return abs(num(vs[0]))
  if f=='MAX':return max(num(x)for x in flat)
  if f=='MIN':return min(num(x)for x in flat)
  if f=='LN':
   x=num(vs[0])
   if x<=0:raise ProbeError('Invalid logarithm')
   return math.log(x)
  if f=='TANH':return math.tanh(num(vs[0]))
  if f in ('COUNTIF','COUNTIFS','SUMIF','SUMIFS'):
   def arr(x):return x if isinstance(x,list)else[x]
   def crit(x,c):
    if isinstance(c,str):
     m=re.match(r'^(<=|>=|<>|=|<|>)(.*)$',c)
     if m:
      op,t=m.groups()
      try:v=float(t)
      except ValueError:v=t
      if op in ('>','<','>=','<='):
       if not isnum(x):return False
       return {'>':x>v,'<':x<v,'>=':x>=v,'<=':x<=v}[op]
      return (x!=v)if op=='<>'else x==v
     if '*'in c or '?'in c:
      import fnmatch
      return isinstance(x,str)and fnmatch.fnmatchcase(x.casefold(),c.casefold())
     return isinstance(x,str)and x.casefold()==c.casefold()
    return x==c
   if f=='COUNTIF':return sum(crit(x,vs[1])for x in arr(vs[0]))
   if f=='SUMIF':return sum(y for x,y in zip(arr(vs[0]),arr(vs[2]if len(vs)>2 else vs[0]))if crit(x,vs[1])and isnum(y))
   start=1 if f=='SUMIFS'else 0;rr=[arr(vs[i])for i in range(start,len(vs),2)];cc=[vs[i]for i in range(start+1,len(vs),2)]
   if len({len(x)for x in rr})!=1:raise ProbeError('Misaligned criterion ranges')
   hits=[all(crit(x,c)for x,c in zip(row,cc))for row in zip(*rr)]
   return sum(y for y,h in zip(arr(vs[0]),hits)if h and isnum(y))if f=='SUMIFS'else sum(hits)
  raise Unsupported('Unsupported function '+f)

def run_probes(path):
 data=inspect(path);results=[]
 cases=[('unchanged',None),('valid_numeric',('Impact_Input','F9',.5,None)),('missing',('Impact_Input','I9',None,None)),('text',('Impact_Input','F9','high',None)),('range',('Impact_Input','F9',1.5,None)),('formula_literal_same',('I_prop','F7',data['cells']['I_prop']['F7']['value'],None)),('formula_same_value',('I_prop','F7',None,str(data['cells']['I_prop']['F7']['value']))),('formula_different_value',('I_prop','F7',None,'0.5')),('version',('Config','B4','SGP v8.7',None)),('saturation_parameter',('Parameters','B24',3,None))]
 for name,change in cases:
  p=WorkbookProbe(data)
  if change:p.set(*change)
  n=p.get('Impact_Input','N9');ip=p.get('I_prop','F7');rls=p.get('Contribution_Analysis','B4');rec=p.get('Build_Integrity','B13');integrity=p.get('Build_Integrity','B14');status=p.get('Build_Integrity','C14')
  expected_intact=name in ('unchanged','formula_same_value')
  ok=(integrity==0)==expected_intact
  if name=='missing':ok=ok and n=='UNKNOWN_INPUT' and rls=='RLS_UNKNOWN_CELLS'
  if name in ('text','range'):ok=ok and n=='INVALID_INPUT' and rls=='INVALID_INPUT'
  if name=='formula_different_value':ok=ok and rec==1 and status=='STALE - REBUILD REQUIRED'
  if name=='unchanged':ok=ok and abs(rls-.0153129427168233)<1e-12
  results.append({'case':name,'input_result':n,'I_prop_F7':ip,'live_RLS_A':rls,'reconciliation':rec,'integrity':integrity,'display':status,'passed':ok,'retained_dependency_caches':sorted(p.frozen_dependencies)})
 return {'status':'PASS'if all(x['passed']for x in results)else'FAIL','executed':len(results),'passed':sum(x['passed']for x in results),'cases':results,'boundary':'Scoped execution of delivered formula strings; selected static dependencies use retained caches independently checked elsewhere. Not a native spreadsheet-engine run, UI validation test or complete XLSX evaluator. Equal-valued formula swaps require the separate exact-file verifier.'}
if __name__=='__main__':
 import sys
 p=Path(sys.argv[1])if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx'
 r=run_probes(p);print(json.dumps(r,indent=2));raise SystemExit(0 if r['status']=='PASS'else 1)
