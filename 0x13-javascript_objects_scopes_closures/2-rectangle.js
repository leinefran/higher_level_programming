#!/usr/bin/node
// an empty class Retangle that defines a rectangle;
// and takes two arguments: width and height;

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
