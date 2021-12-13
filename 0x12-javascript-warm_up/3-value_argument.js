#!/usr/bin/node
const newArgs = process.argv[2];
if (newArgs.length === 2) {
  console.log('No argument');
} else {
  console.log(newArgs);
}
