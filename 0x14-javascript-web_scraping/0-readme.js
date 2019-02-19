#!/usr/bin/node
/* a script that reads and prints the content of a file;
   The first argument is the file path;
   The content of the file must be read in utf-8;
   If an error occurred during the reading, print the error object. */

let fs = require('fs');
fs.readFile(process.argv[2], { encoding: 'utf-8' }, function (err, data) {
  if (!err) {
    console.log(data);
  } else {
    console.log(err);
  }
});
