#!/usr/bin/node

/* Import process module */
const process = require('process');
let len = 0;

/* Calculate length of argv array */
process.argv.forEach((item) => {
  len++;
});

if (len <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
