#!/usr/bin/node
const SquareB = require('./5-square');

class Square extends SquareB {
  charPrint (c = 'X') {
    super.print(c);
  }
}
module.exports = Square;
