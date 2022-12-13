#!/usr/bin/node

const request = require('request');
request
  .get(process.argv[2], function (err, response, body) {
    if (err) {
      console.log(err);
    }
    const tasks = JSON.parse(body);
    const compDict = {};
    tasks.forEach(function (task) {
      if (task.completed && compDict[task.userId] === undefined) {
        compDict[task.userId] = 1;
      } else if (task.completed) {
        compDict[task.userId] += 1;
      }
    });
    console.log(compDict);
  });

  // node 6-completed_tasks.js https://jsonplaceholder.typicode.com/todos