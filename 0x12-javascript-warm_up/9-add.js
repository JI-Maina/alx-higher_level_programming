#!/usr/bin/node
/* prints the addition of 2 integers */

/* import process module */
const process = require('process');

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add (a, b) { console.log(a + b); }

add(a, b);
