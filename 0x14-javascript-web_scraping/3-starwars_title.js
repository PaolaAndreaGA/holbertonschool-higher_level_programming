#!/usr/bin/node

const request = require('request');
const IDMOV = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/:id' + IDMOV;
request.get(URL, function (err, response, list) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(list).title);
  }
});
