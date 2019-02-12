#!/usr/bin/node
// a scrip that prints 2 args passed to it.
// use console.log() to print output.

if (process.argv[2]) {
  console.log(process.argv[2] + ' ' + 'is' + ' ' + process.argv[3]);
} else {
  console.log(process.argv[2] + ' ' + 'is' + ' ' + process.argv[3]);
}
