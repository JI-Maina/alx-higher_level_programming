#!/usr/bin/node
// class Square that defines a square and inherits from Square of 5-square.js
// with an instance method charPrint(c) that prints the Square using the character c or X if c is undefined

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
