const assert=require('node:assert/strict');const {computeField,DEMO}=require('./review_dashboard.js');
let checks=0;const check=(v)=>{assert(v);checks++};
for(const o of ['A','B']){const f=computeField(DEMO.options[o]);check(Math.abs(f.byScope.reduce((a,b)=>a+b)-f.score)<1e-12);check(Math.abs(f.byDimension.reduce((a,b)=>a+b)-f.score)<1e-12);check(f.cells.length===7);}
for(const bad of [NaN,Infinity,2,-2,'0',true]){const p=structuredClone(DEMO.options.A);p.impacts[0][0]=bad;assert.throws(()=>computeField(p));checks++;}
const missing=structuredClone(DEMO.options.A);missing.impacts[0][0]=null;check(computeField(missing).score===null);
const zero=structuredClone(DEMO.options.A);zero.weights=Array.from({length:7},()=>Array(7).fill(0));assert.throws(()=>computeField(zero));checks++;
const neg=structuredClone(DEMO.options.A);neg.weights[0][0]=-1;assert.throws(()=>computeField(neg));checks++;
console.log(JSON.stringify({executed:checks,passed:checks,boundary:'Local JavaScript accounting/input checks; no browser automation or security certification.'},null,2));