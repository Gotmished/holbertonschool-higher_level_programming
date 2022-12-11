#!/usr/bin/node
const superSquare = require('./5-square');

class Square extends superSquare {
  charPrint (c = undefined) {
    if (c === undefined) {
      super.print();
    } else {
      super.print(c);
    }
  }
}
module.exports = Square;
