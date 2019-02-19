#!/usr/bin/node
// a function that returns the reversed version of a list;

exports.esrever = function (list) {
  let reversed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
