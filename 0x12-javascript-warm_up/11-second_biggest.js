#!/usr/bin/node
/* searches the second biggest integer in the list of arguments */

const len = process.argv.length;

if (len <= 3) {
  console.log(0);
} else {
  /* make array copy to arr */
  let arr = [...process.argv];

  /* delete first two elements */
  arr = arr.slice(1);
  arr = arr.slice(1);

  arr.sort(function (a, b) {
    return a - b;
  });

  console.log(arr[arr.length - 2]);
}
