#!/usr/bin/node

/* import process module */
const process = require('process');

/* store the first argument passed */
const len = parseInt(process.argv[2]);

if (!len) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < len; i++) {
  console.log('C is fun');
}
