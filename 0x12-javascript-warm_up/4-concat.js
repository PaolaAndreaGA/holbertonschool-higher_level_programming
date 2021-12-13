#!/usr/bin/node
const concArgs = process.argv;
if (!concArgs) {
  console.log('No argument');
} else {
  console.log(concArgs[2] + ' is ' + concArgs[3]);
}
