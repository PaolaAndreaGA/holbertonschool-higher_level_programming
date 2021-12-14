#!/usr/bin/node
const factArgs = process.argv[2];
function factorial (factArgs) {
  if (isNaN(factArgs) || factArgs === 1) {
    return (1);
  } else {
    return (factArgs * factorial(factArgs - 1));
  }
}
console.log(factorial(parseInt(factArgs)));
