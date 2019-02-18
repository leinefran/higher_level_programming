#!/usr/bin/node
// a class rectangle that defines a rectangle;
// added: two instance methods: rotate(), and double();

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
  rotate () {
    // swap!
    [this.height, this.width] = [this.width, this.height];
  }
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
