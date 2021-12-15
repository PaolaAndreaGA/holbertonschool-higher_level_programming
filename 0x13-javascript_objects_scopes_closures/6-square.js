#!/usr/bin/node
const SquareB = require('./5-square');

class Square extends SquareB {
  charPrint (character = 'X') {
    super.print(character);
  }
}
module.exports = Square;
