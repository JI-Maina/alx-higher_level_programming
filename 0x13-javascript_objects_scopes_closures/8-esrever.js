#!/usr/bin/node
/* function that returns the reversed version of a list */

exports.esrever = function (list) {
  const len = list.length;
  let j = len - 1;
  let temp;
  for (let i = 0; i < j; i++, j--) {
    temp = list[j];
    list[j] = list[i];
    list[i] = temp;
  }

  return list;
};
