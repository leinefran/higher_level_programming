#!/usr/bin/node
/* a script that computes the number of tasks completed by user id.
   The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
   You must use the module request */

const request = require('request');

let url = process.argv[2]

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err); // Print the error if one occurred
  } else {
    let todoList = JSON.parse(body); // todoList is an array of dictionaries;
    let tasks = 0;
    let newDict = {};

    for (let i = 0; i < todoList.length; i++) {
      if (todoList[i].completed === true) {
	newDict[userId] = todoList[i].userId;
      }
  }
});
