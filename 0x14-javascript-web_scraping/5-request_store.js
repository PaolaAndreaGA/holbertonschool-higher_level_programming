#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const DEMO = process.argv[2];
const DEMO2 = process.argv[3];
request(DEMO).pipe(fs.createWriteStream(DEMO2));
