#!/usr/bin/node

const request = require('request');
const DEMO = process.argv[2];
request(DEMO, function (error, response, list) {
  if (!error) {
    const results = JSON.parse(list).results;
    console.log(results.reduce((counter, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? counter + 1
        : counter;
    }, 0));
  }
});
