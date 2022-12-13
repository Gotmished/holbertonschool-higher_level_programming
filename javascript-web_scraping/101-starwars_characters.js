#!/usr/bin/node

const listOrder = [];
const dictValue = {};
const request = require('request');

function urlAssociation (eachUrl) {
  request.get(eachUrl, function (err, response, body) {
    if (err) {
      console.log(err);
    }
    dictValue[eachUrl] = JSON.parse(body).name;
  });
}

request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const characterURL = JSON.parse(body).characters;
  characterURL.forEach(function (eachUrl) {
    listOrder.push(eachUrl);
    urlAssociation(eachUrl);
  });
});
listOrder.forEach(function (url) {
  console.log(dictValue[url]);
});
