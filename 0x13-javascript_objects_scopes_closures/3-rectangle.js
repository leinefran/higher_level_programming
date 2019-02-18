#!/usr/bin/node
// create an instance method called print();
// that prints a rectangle using the character X;

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    console.log('X'.repeat(this.width).concat('\n').repeat(this.height).slice(0, -1));
  }
};
