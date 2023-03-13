#!/usr/bin/node
// import process module
const process = require('process');
const foo = process.argv.length;

if (foo <= 2) {
  console.log('No argument');
} else if (foo === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
