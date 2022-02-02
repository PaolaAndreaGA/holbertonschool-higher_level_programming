#!/usr/bin/node
// prints the characters present in a Star Wars Movie... same order
const request = require('request');

const IDMOV = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/'.concat(IDMOV);

request(URL, function (err, response, list) {
  if (err) { console.error(err); }
  const characters = JSON.parse(list).characters;
  for (let i = 0; characters[i]; i++) {
    request(characters[i], function (err, response, list) {
      if (err) { console.error(err); }
      const name = JSON.parse(list).name;
      console.log(name);
    });
  }
});
