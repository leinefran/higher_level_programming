#!/usr/bin/node
/* a script that prints the number of movies where the character “Wedge Antilles” is present.

The first argument is the API URL of the Star wars API: http://swapi.co/api/films/
Wedge Antilles is character ID 18
You must use the module request */

const request = require('request');

let url = 'http://swapi.co/api/films/';

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err); // Print the error if one occurred
  } else {
    let dic = JSON.parse(body);
    let results = dic['results'];
    console.log(results);
  }
});
