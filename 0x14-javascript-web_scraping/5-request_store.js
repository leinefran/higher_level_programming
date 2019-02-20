#!/usr/bin/node
/* a script that gets the contents of a webpage and stores it in a file.

The first argument is the URL to request
The second argument the file path to store the body response
The file must be UTF-8 encoded
You must use the module request */

const request = require('request');

let url = process.argv[2];
let file = process.argv[3];
const fs = require('fs');

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err); // Print the error if one occurred
  } else {
    fs.writeFile(file, body, { encoding: 'utf-8' }, (err) => {
      // catch error
      if (err) {
        console.log(err);
      }
    });
  }
});
