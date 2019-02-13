#!/usr/bin/node
/* a scrip that prints a square
   using a loop */
// use console.log() to print output.

let size = parseInt(process.argv[2]); // convert to an int;
let i;

if (Number.isInteger(size)) { // checks if number is an int;
  for (i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
