#!/usr/bin/node
/* a scrip that prints: "C is fun" x times.
   using a loop */
// use console.log() to print output.

let myString = 'C is fun';
let x = parseInt(process.argv[2]);
let i;

if (Number.isInteger(x)) {
  for (i = 0; i < x; i++) {
    console.log(myString);
  }
} else {
  console.log('Missing number of occurrences');
}
