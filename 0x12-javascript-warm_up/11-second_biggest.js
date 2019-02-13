#!/usr/bin/node
// a script that searches the 2nd biggest integer in the list of arguments.
// use console.log() to print output.

function sortNumber (a, b) {
  return a - b;
}
let myArray = process.argv;

if (myArray.length <= 3) {
  console.log('0');
} else {
  myArray.sort(sortNumber);
  console.log(myArray[myArray.length - 2]);
}
