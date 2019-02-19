#!/usr/bin/node
/* a script that prints the title of a Star Wars movie where the episode number matches a given integer.

The first argument is the episode number
You must use the Star wars API with the endpoint http://swapi.co/api/films/:id
You must use the module request */

const request = require('request');

let url = 'http://swapi.co/api/films/' + process.argv[2];

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err); // Print the error if one occurred
  } else {
    let dic = JSON.parse(body);
    console.log(dic['title']);
  }
});
