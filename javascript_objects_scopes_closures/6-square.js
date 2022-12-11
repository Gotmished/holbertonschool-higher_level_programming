#!/usr/bin/node
const superSquare = require('./5-square');

class Square extends superSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    super.print(c);
  }
}

module.exports = Square;
