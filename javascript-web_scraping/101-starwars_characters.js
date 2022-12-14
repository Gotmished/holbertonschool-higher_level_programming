#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const characterURL = JSON.parse(body).characters;
  printEach(characterURL, 0);
});

const printEach = function (charactersURL, index) {
  if (index + 1 <= charactersURL.length) {
    request.get(charactersURL[index], function (error, response, body) {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(body).name);
      printEach(charactersURL, index + 1);
    });
  }
};
