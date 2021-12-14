#!/usr/bin/node
exports.esrever = function (list) {
  const myList = [];
  for (let count = 0; list[count]; count++) {
    myList.push(list[list.length - (count + 1)]);
  }
  return (myList);
};
