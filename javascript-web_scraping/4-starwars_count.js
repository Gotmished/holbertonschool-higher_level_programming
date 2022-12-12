#!/usr/bin/node

const request = require('request');
request
  .get(process.argv[2], function (err, response, body) {
    if (err) {
      console.log(err);
    }
    let count = 0;
    const results = JSON.parse(body).results;
    for (const category in results) {
      const characters = results[category].characters;
      for (const eachCharacter in characters) {
        if (characters[eachCharacter].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  });
