/* Local review aid. No network, authority grant, actuator or claimed live telemetry. */
'use strict';
const DEMO = {"kind": "FROZEN_WORKED_EXAMPLE", "source_workbook": "Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx", "source_sha256": "49d9d8fbeb762cb6cddb3ebab402ded25529639f222b665059db297f33b5282c", "evidence_status": "Synthetic worked-run judgments; not empirical calibration", "framework_verdict": "REFUSE_DETERMINISTIC_SELECTION", "authority_note": "Point-score leader A; unvalidated Method C uncertainty flips under the \u03c3\u00d72 stress, so RippleLogic refuses deterministic selection. Option A is separately selected by accountable authority for the bounded worked-run demonstration.", "options": {"A": {"impacts": [[0.0, 0.0, 0.0, 0.0, 0.2490078843274226, 0.1432598557931445, 0.0], [0.046162176234088866, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [-0.01979527432216163, 0.0, -0.08072568681553846, 0.0, 0.0, 0.0, 0.0], [-0.08556943629589667, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01531651795735988]], "weights": [[0.043952380952381034, 0.043952380952381034, 0.043952380952381034, 0.043952380952381034, 0.043952380952381034, 0.043952380952381034, 0.043952380952381034], [0.022333333333333306, 0.022333333333333306, 0.022333333333333306, 0.022333333333333306, 0.022333333333333306, 0.022333333333333306, 0.022333333333333306], [0.017476190476190444, 0.017476190476190444, 0.017476190476190444, 0.017476190476190444, 0.017476190476190444, 0.017476190476190444, 0.017476190476190444], [0.01666666666666673, 0.01666666666666673, 0.01666666666666673, 0.01666666666666673, 0.01666666666666673, 0.01666666666666673, 0.01666666666666673], [0.013047619047619054, 0.013047619047619054, 0.013047619047619054, 0.013047619047619054, 0.013047619047619054, 0.013047619047619054, 0.013047619047619054], [0.014771428571428586, 0.014771428571428586, 0.014771428571428586, 0.014771428571428586, 0.014771428571428586, 0.014771428571428586, 0.014771428571428586], [0.01460952380952387, 0.01460952380952387, 0.01460952380952387, 0.01460952380952387, 0.01460952380952387, 0.01460952380952387, 0.01460952380952387]]}, "B": {"impacts": [[0.0, 0.0, 0.0, 0.0, -0.046333567670633624, 0.0, 0.0], [-0.01847590043753792, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.013197807340577457, 0.0, 0.06151557221350915, 0.0, 0.0, 0.0, 0.0], [0.010211455619172161, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.010211455619172184]], "weights": [[0.043952380952381034, 0.043952380952381034, 0.043952380952381034, 0.043952380952381034, 0.043952380952381034, 0.043952380952381034, 0.043952380952381034], [0.022333333333333306, 0.022333333333333306, 0.022333333333333306, 0.022333333333333306, 0.022333333333333306, 0.022333333333333306, 0.022333333333333306], [0.017476190476190444, 0.017476190476190444, 0.017476190476190444, 0.017476190476190444, 0.017476190476190444, 0.017476190476190444, 0.017476190476190444], [0.01666666666666673, 0.01666666666666673, 0.01666666666666673, 0.01666666666666673, 0.01666666666666673, 0.01666666666666673, 0.01666666666666673], [0.013047619047619054, 0.013047619047619054, 0.013047619047619054, 0.013047619047619054, 0.013047619047619054, 0.013047619047619054, 0.013047619047619054], [0.014771428571428586, 0.014771428571428586, 0.014771428571428586, 0.014771428571428586, 0.014771428571428586, 0.014771428571428586, 0.014771428571428586], [0.01460952380952387, 0.01460952380952387, 0.01460952380952387, 0.01460952380952387, 0.01460952380952387, 0.01460952380952387, 0.01460952380952387]]}}, "appendix_release": {"framework": "MathGov/RippleLogic v13.0", "profile": "Local review interface 1.0"}};
const DIMS=['Material','Health','Social','Knowledge','Agency','Meaning','Environment'];
const SCOPES=['Self','Family / Household','Community','Organization','Polity','Humanity / CMIU views','Biosphere'];
function computeField(input){
  if(!input || !Array.isArray(input.impacts) || !Array.isArray(input.weights) || input.impacts.length!==7 || input.weights.length!==7)throw new Error('Expected seven scope rows.');
  let mass=0,unknown=false;
  for(let i=0;i<7;i++){
    if(!Array.isArray(input.impacts[i]) || !Array.isArray(input.weights[i]) || input.impacts[i].length!==7 || input.weights[i].length!==7)throw new Error('Expected seven dimensions per row.');
    for(let j=0;j<7;j++){
      const x=input.impacts[i][j],w=input.weights[i][j];
      if(typeof w!=='number' || !Number.isFinite(w) || w<0)throw new Error('Weight must be finite and nonnegative.');
      if(x===null)unknown=true;else if(typeof x!=='number'||!Number.isFinite(x)||x< -1||x>1)throw new Error('Impact must be signed [-1,1] or explicit null.');
      mass+=w;
    }
  }
  if(!(mass>0))throw new Error('RLS_NO_ACTIVE_MASS');
  const cells=input.impacts.map((row,i)=>row.map((x,j)=>x===null?null:x*input.weights[i][j]/mass));
  const sum=xs=>xs.some(x=>x===null)?null:xs.reduce((a,b)=>a+b,0);
  const byScope=cells.map(sum),byDimension=DIMS.map((_,j)=>sum(cells.map(row=>row[j])));
  return {mass,cells,byScope,byDimension,score:unknown?null:sum(byScope)};
}
if(typeof module!=='undefined' && module.exports)module.exports={computeField,DEMO};
if(typeof document!=='undefined'){
 let current=DEMO;
 const el=id=>document.getElementById(id);
 const fmt=x=>x===null?'UNKNOWN':(x>0?'+':'')+x.toFixed(6);
 function td(text,cls=''){const x=document.createElement('td');x.textContent=text;if(cls)x.className=cls;return x;}
 function render(){
  try{
   const opt=el('option').value,p=current.options[opt],f=computeField(p);el('error').textContent='';
   el('score').textContent=f.score===null?'RLS unavailable':fmt(f.score);el('mass').textContent=f.mass.toPrecision(8);
   el('verdict').textContent=current.framework_verdict || 'NOT PROVIDED';el('evidence').textContent=current.evidence_status || 'NOT PROVIDED';
   el('authority').textContent=current.authority_note || 'No authority record provided.';
   el('source').textContent=(current.source_workbook || 'User-supplied snapshot')+' | SHA-256 declared: '+(current.source_sha256 || 'NOT PROVIDED');
   const body=el('matrix-body');body.replaceChildren();
   f.cells.forEach((row,i)=>{const tr=document.createElement('tr');const th=document.createElement('th');th.scope='row';th.textContent='U'+(i+1)+' '+SCOPES[i];tr.append(th);row.forEach((x,j)=>{let cell=td(fmt(x),x===null?'unknown':x<0?'negative':x>0?'positive':'');cell.title='I = '+fmt(p.impacts[i][j])+'; effective weight = '+p.weights[i][j];tr.append(cell);});tr.append(td(fmt(f.byScope[i]),'total'));body.append(tr);});
   const tr=document.createElement('tr');const th=document.createElement('th');th.scope='row';th.textContent='Dimension total';tr.append(th);f.byDimension.forEach(x=>tr.append(td(fmt(x),'total')));tr.append(td(fmt(f.score),'total'));body.append(tr);
  }catch(e){el('error').textContent=e.message;el('score').textContent='UNAVAILABLE';el('matrix-body').replaceChildren();}
 }
 el('option').addEventListener('change',render);
 el('load').addEventListener('change',async event=>{try{const file=event.target.files[0];if(!file)return;if(file.size>2000000)throw new Error('Snapshot exceeds local 2 MB limit.');const p=JSON.parse(await file.text());if(!p.options?.A||!p.options?.B)throw new Error('This reading aid requires named A and B options.');computeField(p.options.A);computeField(p.options.B);current=p;render();}catch(e){el('error').textContent=e.message;}});
 render();
}
