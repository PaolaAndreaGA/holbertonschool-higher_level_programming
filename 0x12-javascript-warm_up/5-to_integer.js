#!/usr/bin/node
const numArgs = process.argv[2];
if (!numArgs) {
  console.log('Not a number');
} else if (parseInt(numArgs)) {
  console.log('My number: ' + Math.floor(numArgs));
} else {
  console.log('Not a number');
}
