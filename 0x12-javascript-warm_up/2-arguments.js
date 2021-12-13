#!/usr/bin/node
const neWArgs = process.argv;
if (neWArgs.length === 2) {
  console.log('No argument');
} else if (neWArgs.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
