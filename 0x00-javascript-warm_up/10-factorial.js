#!/usr/bin/node

function factorial (x) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
