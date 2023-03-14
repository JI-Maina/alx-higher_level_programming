#!/usr/bin/node
/* script that imports an array and computes a new array */

const list = require('./100-data').list;
const len = list.length;
let newList = [];

newList = list.map(item => item);

for (let i = 0; i < len; i++) {
  newList[i] = newList[i] * i;
}

console.log(list);
console.log(newList);
