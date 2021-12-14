#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let count = 0; list[count]; count++) {
    if (searchElement === list[count]) {
      counter++;
    }
  }
  return counter;
};
