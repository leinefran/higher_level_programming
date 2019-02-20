#!/usr/bin/node
/* a script that prints the number of movies where the character “Wedge Antilles” is present.
The first argument is the API URL of the Star wars API: http://swapi.co/api/films/
Wedge Antilles is character ID 18
You must use the module request */

const request = require('request');

let url = 'http://swapi.co/api/films/';

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err); // Print the error if one ocurred;
  } else {
    let count = 0;
    let dic = JSON.parse(body).results;
    for (let k of dic) {
      for (let key of k.characters) {
        if (key.includes('18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
