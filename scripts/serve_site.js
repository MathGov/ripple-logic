// Local test server. Bind to loopback and serve only the generated site.
const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '../_site');
const types = {'.html':'text/html', '.css':'text/css', '.js':'text/javascript', '.json':'application/json'};
http.createServer((req, res) => {
  let filename;
  try { filename = path.resolve(root, '.' + decodeURIComponent(new URL(req.url, 'http://localhost').pathname)); }
  catch { res.writeHead(400); res.end(); return; }
  if (filename !== root && !filename.startsWith(root + path.sep)) { res.writeHead(403); res.end(); return; }
  if (fs.existsSync(filename) && fs.statSync(filename).isDirectory()) filename = path.join(filename, 'index.html');
  fs.readFile(filename, (error, data) => {
    if (error) { res.writeHead(404); res.end('Not found'); return; }
    res.setHeader('Content-Type', (types[path.extname(filename)] || 'application/octet-stream') + '; charset=utf-8');
    res.end(data);
  });
}).listen(4173, '127.0.0.1');
