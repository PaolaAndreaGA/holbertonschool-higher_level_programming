#!/usr/bin/node

const fs = require('fs');
const Demo = process.argv[2];
fs.readFile(Demo, 'utf8', function(err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
