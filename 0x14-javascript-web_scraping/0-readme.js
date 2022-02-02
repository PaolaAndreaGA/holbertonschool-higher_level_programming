#!/usr/bin/node

const fs = require('fs');
<<<<<<< HEAD
const demo = process.argv[2];
fs.readFile(demo, 'utf8', function(err, data) {
=======
const Demo = process.argv[2];
fs.readFile(Demo, 'utf8', function(err, data) {
>>>>>>> 44aa2f23e05ed03d3dc6f76fd8e29ee451deef22
  if (err) {
    console.log(err);
  } else {
	console.log(data);
  }
});
