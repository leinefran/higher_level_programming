#!/usr/bin/node
/* The first argument is the file path
The second argument is the string to write
The content of the file must be written in utf-8
If an error occurred during while writing, print the error object */

const fs = require('fs');

let text = process.argv[3];

fs.writeFile(process.argv[2], text, { encoding: 'utf-8' }, (err) => {
  // catch error
  if (err) {
    console.log(err);
  }
});
