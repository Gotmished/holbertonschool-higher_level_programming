#!/usr/bin/node

const request = require('request');
request
  .get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, response, body) {
    if (err) {
      console.log(err);
    }
    const characters = JSON.parse(body).characters;
    characters.forEach(function (characterURL) {
      request.get(characterURL, function (err, response, body) {
        if (err) {
          console.log(err);
        }
        console.log(JSON.parse(body).name);
      });
    });
  });
