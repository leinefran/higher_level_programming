#!/usr/bin/node
/* a scrip that prints:
   "C is fun"
   "Python is cool"
   "Javascript is amazing"
   using a lopp */

// use console.log() to print output.

let myArray = ['C is fun', 'Python is cool', 'Javascript is amazing'];
let index = 0;

while (index < myArray.length) {
  console.log(myArray[index]);
  index++;
}
