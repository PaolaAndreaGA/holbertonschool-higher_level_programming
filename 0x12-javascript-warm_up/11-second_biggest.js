#!/usr/bin/node
const lenArgs = process.argv.length;
if (lenArgs < 4) {
  console.log('0');
} else {
  const num = process.argv.sort((a, b) => a - b);
  console.log(num[num.length - 2]);
}
