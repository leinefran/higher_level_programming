#!/usr/bin/node
/* a script that computes the number of tasks completed by user id.
   The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
   You must use the module request */

const request = require('request');

let url = process.argv[2]

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err); // Print the error if one occurred
  }
  let newObj = {};
  // todoList is an array of dictionaries;
  let todoList = JSON.parse(body).forEach(function(item) {
    if(item.completed) {
       newObj[item.userId] ? newObj[item.userId] += 1 : newObj[item.userId] = 1;
    }
  });
  console.log(newObj)
});
