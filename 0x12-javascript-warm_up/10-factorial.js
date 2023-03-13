#!/usr/bin/node
/* computes and prints a factorial */

/* import process module */
const process = require('process');

const num = parseInt(process.argv[2]);

if (!num) {
  console.log(1);
} else {
  function calcFactorial (num) {
    if (num <= 1) {
      return 1;
    } else {
      return num * calcFactorial(num - 1);
    }
  }
  const fact = calcFactorial(num);
  console.log(fact);
}
