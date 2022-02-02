#!/usr/bin/node
const request = require('request');
const DEMO = process.argv[2];
request(DEMO, function (error, response, body) {
  if (!error) {
    const every = JSON.parse(body);
    const completed = {};
    every.forEach((all) => {
      if (all.completed && completed[all.userId] === undefined) {
        completed[all.userId] = 1;
      } else if (all.completed) {
        completed[all.userId] += 1;
      }
    });
    console.log(completed);
  }
});
