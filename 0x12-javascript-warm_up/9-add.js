#!/usr/bin/node
const addA = process.argv[2];
const addB = process.argv[3];
if (!addA || !addB) {
  console.log('NaN');
} else {
  const add = parseInt(addA) + parseInt(addB);
  console.log(add);
}
