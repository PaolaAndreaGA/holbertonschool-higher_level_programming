#!/usr/bin/node

const request = require('request');

const URL = 'https://swapi-api.hbtn.io/api/films/';
request(URL + process.argv[2], function (err, response, list) {
  console.log(err || JSON.parse(list).title);
});
