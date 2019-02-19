#!/usr/bin/node
// a class Square that defines a square and inherits from Square of 5-square.js;

let s1 = require('./5-square');
module.exports = class Square extends s1 {
  charPrint (c) {
    if (c) {
      console.log(c.repeat(this.width).concat('\n').repeat(this.height).slice(0, -1));
    } else {
      console.log('X'.repeat(this.width).concat('\n').repeat(this.height).slice(0, -1));
    }
  }
};
