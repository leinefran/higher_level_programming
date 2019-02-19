#!/usr/bin/node
// a function that prints the number of arguments already printed and the argument value;

let countPrint = 0;
exports.logMe = function (item) {
  if (item) {
    console.log(countPrint + ': ' + item);
    countPrint += 1;
  }
};
