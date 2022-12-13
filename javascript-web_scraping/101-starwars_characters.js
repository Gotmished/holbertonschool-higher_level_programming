#!/usr/bin/node

const listOrder = [];
const dictValue = {};
const request = require('request');

request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const characterURL = JSON.parse(body).characters;
  listOrder.push(characterURL);
  characterURL.forEach(function (eachUrl) {
    request.get(eachUrl, function (err, response, body) {
      if (err) {
        console.log(err);
      }
      dictValue[eachUrl] = JSON.parse(body).name;
    });
  });
  listOrder.forEach(function (url) {
    console.log(dictValue[url]);
  });
});
