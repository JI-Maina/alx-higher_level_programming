#!/usr/bin/node
/* script that imports an array and computes a new array */

const list = require('./100-data').list;

let newList = [];

newList = list.map((item, index) => {
  return item * index;
});

console.log(list);
console.log(newList);
