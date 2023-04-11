#!/usr/bin/node

const Rectangle = require("./1-rectangle.js");

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};

module.exports = Square;
