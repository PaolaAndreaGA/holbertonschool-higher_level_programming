#!/usr/bin/node
const loopArgs = process.argv[2];
if (parseInt(loopArgs)) {
  for (let x = 0; x < loopArgs; x++) {
    console.log('X'.repeat(loopArgs));
  }
} else {
  console.log('Missing size');
}
