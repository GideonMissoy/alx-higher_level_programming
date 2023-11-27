#!/usr/bin/node
const fs = require('fs');
const q = fs.readFileSync(process.argv[2], 'utf8');
const r = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], p + q);
