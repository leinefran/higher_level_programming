#!/usr/bin/node
/* a scrip that prints the addition of 2 integers
   using a loop
   The first argument is the first integer
   The second argument is the second integer
   use console.log() to print output */

function add(a, b) {

  let sum = +a + +b;
  console.log(sum);
  return sum;
}
add(process.argv[2], process.argv[3]);
