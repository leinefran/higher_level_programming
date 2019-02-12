#!/usr/bin/node
// a scrip that prints the first argument passed to it.
// use console.log() to print output.

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
