#!/usr/bin/node
/* a scrip that prints: My number: <first argument converted in integer>
   if the first arg can be converted to an int */
// use console.log() to print output.

let data = parseInt(process.argv[2]);

if (Number.isInteger(data)) {
  console.log('My number: ' + data);
} else {
  console.log('Not a number');
}
