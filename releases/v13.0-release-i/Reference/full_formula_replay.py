"""Re-evaluate the exact formula corpus in the frozen Aligners workbook.

This is a deliberately scoped reference evaluator, not Microsoft Excel or
LibreOffice compatibility certification. It reads literals and formula text,
never formula cached results during evaluation. Unsupported functions/syntax
raise errors, even within IFERROR, rather than silently consuming a cache.
The original workbook is not modified. The output ledger is saved/reopened JSON.
"""
from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from functools import lru_cache
from collections import Counter
import argparse, hashlib, json, math, re, xml.etree.ElementTree as X
from zipfile import ZipFile
from Workbook_Verifier import inspect
from workbook_probe import parse, colno, colname, Unsupported
ROOT=Path(__file__).resolve().parents[1]
class FormulaError(ValueError): pass
@dataclass
class Ref:
    cells:list[tuple[str,str]]
    columns:int=1
class Evaluator:
    def __init__(self,data,names=None):
        self.data=data;self.names=names or {};self.memo={};self.stack=set();self.functions=Counter();self.formula_reads=0
        self.lastrow={s:max((int(re.search(r'\d+$',c).group()) for c in cs),default=1) for s,cs in data['cells'].items()}
    def clone_with(self,s,c,value=None,formula=None):
        from copy import deepcopy
        d=deepcopy(self.data);d['cells'].setdefault(s,{})[c]={**d['cells'].get(s,{}).get(c,{}),'value':value,'formula':formula}
        return Evaluator(d,self.names)
    def cell(self,s,c):return self.data['cells'].get(s,{}).get(c,{})
    def reference(self,s,a,b):
        if a in self.names and a==b:return self.eval(parse(self.names[a]),s)
        def addr(v):
            m=re.fullmatch(r'([A-Z]+)(\d*)',v)
            if not m:raise Unsupported('Reference '+v)
            return colno(m[1]),int(m[2]) if m[2] else None
        c1,r1=addr(a);c2,r2=addr(b);r1=1 if r1 is None else r1;r2=self.lastrow[s] if r2 is None else r2
        return Ref([(s,colname(c)+str(r)) for r in range(r1,r2+1) for c in range(c1,c2+1)],c2-c1+1)
    def get(self,s,c):
        k=(s,c)
        if k in self.memo:return self.memo[k]
        if k in self.stack:raise FormulaError('Circular reference '+s+'!'+c)
        e=self.cell(s,c)
        if e.get('formula') is None:
            if e.get('type')=='e':raise FormulaError(str(e.get('value')))
            return e.get('value')
        self.stack.add(k);self.formula_reads+=1
        try:
            v=self.scalar(self.eval(parse(e['formula']),s));v=0. if v is None else v
            if isinstance(v,float) and not math.isfinite(v):raise FormulaError('Nonfinite formula result')
            self.memo[k]=v;return v
        finally:self.stack.remove(k)
    def scalar(self,v):
        if isinstance(v,FormulaError):raise v
        if isinstance(v,Ref):
            if len(v.cells)!=1:raise Unsupported('Implicit range intersection not implemented')
            return self.get(*v.cells[0])
        return v
    def vector(self,v):
        if isinstance(v,Ref):return [self.get(*c) for c in v.cells]
        return v if isinstance(v,list) else [v]
    def number(self,v):
        v=self.scalar(v)
        if v is None:return 0.
        if isinstance(v,(int,float)):return float(v)
        raise FormulaError('Nonnumeric arithmetic')
    def string(self,v):
        v=self.scalar(v)
        if v is None:return ''
        if type(v) is bool:return 'TRUE' if v else 'FALSE'
        if isinstance(v,(int,float)):return format(v,'.15g')
        return str(v)
    def logical(self,v):
        v=self.scalar(v)
        if v in (None,''):return False
        if isinstance(v,str):
            if v.upper() in ('TRUE','FALSE'):return v.upper()=='TRUE'
            raise FormulaError('Invalid logical string')
        return bool(v)
    def lift(self,fn,*vals):
        vec=[self.vector(x) for x in vals];n=max(map(len,vec),default=1)
        if any(len(x)not in(1,n)for x in vec):raise FormulaError('Shape mismatch')
        out=[fn(*(x[0]if len(x)==1 else x[i]for x in vec))for i in range(n)]
        return out if n>1 else out[0]
    def compare(self,l,r,op):
        l=self.scalar(l);r=self.scalar(r)
        if l is None:l=''if isinstance(r,str)else 0
        if r is None:r=''if isinstance(l,str)else 0
        if isinstance(l,str)and isinstance(r,str):l,r=l.casefold(),r.casefold()
        def rank(v):return 2 if isinstance(v,bool)else 1 if isinstance(v,str)else 0
        if type(l)!=type(r)and rank(l)!=rank(r):l,r=rank(l),rank(r)
        return {'=':lambda:l==r,'<>':lambda:l!=r,'<':lambda:l<r,'>':lambda:l>r,'<=':lambda:l<=r,'>=':lambda:l>=r}[op]()
    def criterion(self,v,c):
        if isinstance(c,str):
            m=re.match(r'^(<=|>=|<>|=|<|>)(.*)$',c)
            if m:
                op,c=m.groups()
                try:c=float(c)
                except ValueError:pass
                if op in('<','>','<=','>=')and type(v)not in(int,float):return False
                return self.compare(v,c,op)
            if '*'in c or '?'in c:
                pattern='';i=0
                while i<len(c):
                    if c[i]=='~'and i+1<len(c):i+=1;pattern+=re.escape(c[i])
                    elif c[i]=='*':pattern+='.*'
                    elif c[i]=='?':pattern+='.'
                    else:pattern+=re.escape(c[i])
                    i+=1
                return bool(re.fullmatch(pattern,self.string(v),re.I))
        return self.compare(v,c,'=')
    def eval(self,a,s):
        typ=a[0]
        if typ=='value':return a[1]
        if typ=='ref':return self.reference(a[1]or s,a[2],a[3])
        if typ=='unary':return self.lift(lambda v:self.number(v)*(1 if a[1]=='+'else -1),self.eval(a[2],s))
        if typ=='op':
            op=a[1];l=self.eval(a[2],s);r=self.eval(a[3],s)
            if op=='&':return self.lift(lambda x,y:self.string(x)+self.string(y),l,r)
            if op in('=','<>','<','>','<=','>='):return self.lift(lambda x,y:self.compare(x,y,op),l,r)
            def ar(x,y):
                x,y=self.number(x),self.number(y)
                if op=='+':return x+y
                if op=='-':return x-y
                if op=='*':return x*y
                if op=='/':
                    if y==0:raise FormulaError('Division by zero')
                    return x/y
                if op=='^':return x**y
                raise Unsupported('Operator '+op)
            return self.lift(ar,l,r)
        if typ!='call':raise Unsupported(str(a))
        f,args=a[1],a[2];self.functions[f]+=1
        if f=='IF':return self.eval(args[1]if self.logical(self.eval(args[0],s))else args[2],s)
        if f=='IFERROR':
            try:return self.scalar(self.eval(args[0],s))
            except FormulaError:return self.eval(args[1],s)
        if f in('TRUE','FALSE'):return f=='TRUE'
        v=[self.eval(x,s)for x in args]
        if f=='INDEX':
            ar=v[0]
            if not isinstance(ar,Ref):raise Unsupported('INDEX requires range')
            row=int(self.number(v[1]));col=int(self.number(v[2]))if len(v)>2 else 1
            if len(v)==2 and ar.columns==len(ar.cells):row,col=1,row
            idx=(row-1)*ar.columns+col-1
            if row<1 or col<1 or col>ar.columns or not 0<=idx<len(ar.cells):raise FormulaError('INDEX bounds')
            return Ref([ar.cells[idx]])
        if f=='ISBLANK':
            ar=v[0]
            if isinstance(ar,Ref):return all(self.cell(*r).get('formula')is None and self.cell(*r).get('value')is None for r in ar.cells)
            return self.scalar(ar)is None
        if f=='ISFORMULA':
            if not isinstance(v[0],Ref):return False
            return all(self.cell(*r).get('formula')is not None for r in v[0].cells)
        if f=='ROW':
            if not v or not isinstance(v[0],Ref):raise Unsupported('ROW requires explicit reference')
            rows=[int(re.search(r'\d+$',c).group())for sn,c in v[0].cells]
            return rows if len(rows)>1 else rows[0]
        if f=='ISNUMBER':return self.lift(lambda x:type(x)in(int,float)and math.isfinite(x),v[0])
        if f=='ISTEXT':return self.lift(lambda x:isinstance(x,str),v[0])
        if f=='TYPE':return self.lift(lambda x:4 if type(x)is bool else 2 if isinstance(x,str)else 1,v[0])
        if f=='EXACT':return self.lift(lambda x,y:self.string(x)==self.string(y),*v)
        if f=='LEN':return self.lift(lambda x:len(self.string(x)),v[0])
        if f=='TRIM':return self.lift(lambda x:re.sub(' +',' ',self.string(x).strip(' ')),v[0])
        if f=='UPPER':return self.lift(lambda x:self.string(x).upper(),v[0])
        if f=='LOWER':return self.lift(lambda x:self.string(x).lower(),v[0])
        if f=='LEFT':return self.lift(lambda x,n:self.string(x)[:int(self.number(n))],v[0],v[1]if len(v)>1 else 1)
        if f=='MID':return self.lift(lambda x,n,c:self.string(x)[int(self.number(n))-1:int(self.number(n))-1+int(self.number(c))],*v)
        if f=='SEARCH':
            def search(x,y):
                i=self.string(y).casefold().find(self.string(x).casefold())
                if i<0:raise FormulaError('SEARCH not found')
                return i+1
            # Errors inside array ISNUMBER are represented for this function only.
            def safe(x,y):
                try:return search(x,y)
                except FormulaError:return FormulaError('SEARCH not found')
            return self.lift(safe,*v)
        if f=='MATCH':
            if len(v)<3 or self.number(v[2])!=0:raise Unsupported('Only exact MATCH is supported')
            for i,x in enumerate(self.vector(v[1]),1):
                if self.compare(self.scalar(v[0]),x,'='):return i
            raise FormulaError('MATCH not found')
        if f=='VLOOKUP':
            ar=v[1]
            if not isinstance(ar,Ref)or len(v)!=4 or self.logical(v[3]):raise Unsupported('Only exact VLOOKUP is supported')
            col=int(self.number(v[2]));key=self.scalar(v[0])
            if not 1<=col<=ar.columns:raise FormulaError('VLOOKUP column')
            for i in range(0,len(ar.cells),ar.columns):
                if self.compare(key,self.get(*ar.cells[i]),'='):return self.get(*ar.cells[i+col-1])
            raise FormulaError('VLOOKUP not found')
        flat=[x for z in v for x in self.vector(z)]
        for item in flat:
            if isinstance(item,FormulaError):raise item
        if f=='AND':return all(self.logical(x)for x in flat)
        if f=='OR':return any(self.logical(x)for x in flat)
        if f=='NOT':return not self.logical(v[0])
        if f=='COUNT':return sum(type(x)in(int,float)for x in flat)
        if f=='COUNTA':return sum(x is not None for x in flat)
        if f=='COUNTBLANK':return sum(x is None or x==''for x in flat)
        if f=='SUM':return sum(x for x in flat if type(x)in(int,float))
        if f in('MAX','MIN'):
            nums=[x for x in flat if type(x)in(int,float)];return (max(nums)if f=='MAX'else min(nums))if nums else 0.
        if f=='SUMPRODUCT':
            vectors=[self.vector(x)for x in v]
            if len(set(map(len,vectors)))!=1:raise FormulaError('SUMPRODUCT shape')
            return sum(math.prod(x if type(x)in(int,float)else 0 for x in row)for row in zip(*vectors))
        if f=='ROUND':return float(Decimal(str(self.number(v[0]))).quantize(Decimal(1).scaleb(-int(self.number(v[1]))),rounding=ROUND_HALF_UP))
        if f=='ABS':return abs(self.number(v[0]))
        if f=='LN':
            n=self.number(v[0])
            if n<=0:raise FormulaError('LN domain')
            return math.log(n)
        if f=='TANH':return math.tanh(self.number(v[0]))
        if f in('COUNTIF','COUNTIFS','SUMIF','SUMIFS'):
            if f in('COUNTIF','SUMIF'):
                ar=self.vector(v[0]);hits=[self.criterion(x,self.scalar(v[1]))for x in ar]
                vals=self.vector(v[2])if len(v)>2 else ar
            else:
                start=1 if f=='SUMIFS'else 0;arrays=[self.vector(v[i])for i in range(start,len(v),2)];cs=[self.scalar(v[i])for i in range(start+1,len(v),2)]
                if len(set(map(len,arrays)))!=1:raise FormulaError('Conditional range shape')
                hits=[all(self.criterion(x,c)for x,c in zip(row,cs))for row in zip(*arrays)];vals=self.vector(v[0])
            if f.startswith('COUNT'):return sum(hits)
            if len(vals)!=len(hits):raise FormulaError('Sum range shape')
            return sum(x for x,yes in zip(vals,hits)if yes and type(x)in(int,float))
        raise Unsupported('Function '+f)

def equal(a,b):
    if type(a)in(int,float)and type(b)in(int,float):return math.isclose(a,b,abs_tol=1e-12,rel_tol=1e-10)
    return type(a)==type(b)and a==b

def replay(path,output=None):
    data=inspect(path);ev=Evaluator(data);rows=[];errors=[];mismatch=[]
    for s,cs in data['cells'].items():
        for c,x in cs.items():
            if x.get('formula')is None:continue
            try:
                v=ev.get(s,c);match=equal(v,x['value']);rows.append({'sheet':s,'cell':c,'result':v,'cache':x['value'],'match':match})
                if not match:mismatch.append(rows[-1])
            except Exception as exc:errors.append({'sheet':s,'cell':c,'error':type(exc).__name__+': '+str(exc)})
    result={'status':'PASS'if not errors and not mismatch else'FAIL','workbook_sha256':data['sha256'],'formula_count':data['formula_count'],'evaluated':len(rows),'cached_formula_dependencies_used':0,'formula_errors':errors,'mismatches':mismatch,'functions_executed':dict(ev.functions),'tolerance':{'absolute':1e-12,'relative':1e-10},'boundary':'Scoped replay of this workbook formula corpus. Not a general spreadsheet engine, evidence validation, native Excel/LibreOffice parity or production conformance.'}
    if output:
        output=Path(output);output.mkdir(parents=True,exist_ok=True)
        ledger=output/'formula_results.json';ledger.write_text(json.dumps(rows,ensure_ascii=False,indent=2));result['result_ledger_sha256']=hashlib.sha256(ledger.read_bytes()).hexdigest();result['saved_ledger_reopened']=json.loads(ledger.read_text())==rows
        (output/'formula_replay_receipt.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    return result
if __name__=='__main__':
    a=argparse.ArgumentParser(description=__doc__);a.add_argument('--workbook',type=Path,default=ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx');a.add_argument('--output-dir',type=Path);args=a.parse_args()
    r=replay(args.workbook,args.output_dir);print(json.dumps(r,indent=2));raise SystemExit(0 if r['status']=='PASS'else 1)
