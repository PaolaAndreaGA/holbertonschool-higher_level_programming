#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(URL, function (error, response, list) {
  if (!error) {
    const characters = JSON.parse(list).characters;
    characters.forEach((character) => {
      request(character, function (error, response, list) {
        if (!error) {
          console.log(JSON.parse(list).name);
        }
      });
    });
  }
});
