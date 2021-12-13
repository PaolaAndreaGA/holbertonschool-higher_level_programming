#!/usr/bin/node
const newArgs = process.argv[2];
if (!newArgs) {
  console.log('No argument');
} else {
  console.log(newArgs);
}
