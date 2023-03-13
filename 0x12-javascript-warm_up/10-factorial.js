#!/usr/bin/node
/* computes and prints a factorial */

function calcFactorial (num) {
  if (!parseInt(num)) {
    return 1;
  }

  if (num <= 1) {
    return 1;
  } else {
    return num * calcFactorial(num - 1);
  }
}

console.log(calcFactorial(process.argv[2]));
