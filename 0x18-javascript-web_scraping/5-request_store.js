#!/usr/bin/node

const request = require('request');
const fs = require('fs');
request.get(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(process.argv[3], body, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});

// node 5-request_store.js http://loripsum.net/api loripsum
