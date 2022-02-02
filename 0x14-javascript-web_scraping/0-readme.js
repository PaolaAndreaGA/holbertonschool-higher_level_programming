#!/usr/bin/node

const fs = require('fs');
const demo = process.argv[2];
fs.readFile(demo, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
