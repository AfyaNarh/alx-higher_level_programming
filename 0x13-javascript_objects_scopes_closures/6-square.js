#!/usr/bin/node
/**
 *quare class that inherits from previous square class
 */
const PrevSquare = require('./5-square');

classquare extends PrevSquare {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let y = 0;
      while (y < this.width) {
        myVar += myChar;
        y++;
      }

      console.log(myVar);
    }
  }
}

module.exports =quare;
