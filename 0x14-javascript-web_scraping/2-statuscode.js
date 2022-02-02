#!/usr/bin/node

const request = require('request');
const DEMO = process.argv[2];
request(DEMO, function (err, response) {
  if (err) throw err;
  console.log('code:', response && response.statusCode);
});
