const {Graphviz}=require('@hpcc-js/wasm-graphviz');
const fs=require('fs'), path=require('path');
const src=process.argv[2], out=process.argv[3];
Graphviz.load().then(g=>{
  const svg=g.layout(fs.readFileSync(src,'utf8'),'svg','dot');
  fs.writeFileSync(out,svg);
  const m=svg.match(/viewBox="([^"]+)"/);
  console.log(path.basename(out),'|',svg.length,'bytes | viewBox',m?m[1]:'?');
}).catch(e=>{console.error('ERROR:',e.message);process.exit(1)});
