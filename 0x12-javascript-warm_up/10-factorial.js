#!/usr/bin/node
// a script that computes and prints a factorial:

// recursive
let factorial = function (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
};
// function call:
console.log(factorial(parseInt(process.argv[2])));
