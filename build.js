// build.js — copies frontend files into public/ for Vercel static serving
const fs = require('fs');
const path = require('path');

const SRC = __dirname;
const DEST = path.join(__dirname, 'public');

// Files and directories to include in the Vercel output
const INCLUDE = [
  'index.html',
  'compiler.html',
  'history.html',
  'about.html',
  'assets',
  'frontend',
];

function copyRecursive(src, dest) {
  const stat = fs.statSync(src);
  if (stat.isDirectory()) {
    fs.mkdirSync(dest, { recursive: true });
    for (const entry of fs.readdirSync(src)) {
      copyRecursive(path.join(src, entry), path.join(dest, entry));
    }
  } else {
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.copyFileSync(src, dest);
  }
}

// Clean and recreate public/
if (fs.existsSync(DEST)) fs.rmSync(DEST, { recursive: true });
fs.mkdirSync(DEST);

for (const item of INCLUDE) {
  const src = path.join(SRC, item);
  const dest = path.join(DEST, item);
  if (fs.existsSync(src)) {
    copyRecursive(src, dest);
    console.log(`copied: ${item}`);
  } else {
    console.warn(`skipped (not found): ${item}`);
  }
}

console.log('Build complete → public/');
