#!/usr/bin/node
/* a script that display the status code of a GET request;
The first argument is the URL to request (GET)
The status code must be printed like this: code: <status code>
You must use the module request */

const request = require('request');

request.get(process.argv[2], function (err, res) {
  if (err) {
    console.log(err); // Print the error if one occurred
  } else {
    console.log('code :', res.statusCode); // Print the res status code
  }
});
