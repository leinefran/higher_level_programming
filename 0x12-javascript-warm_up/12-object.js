#!/usr/bin/node
// a script to replace the value 12 with 89.
// use console.log() to print output.

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject['value'] = 89;
console.log(myObject);
