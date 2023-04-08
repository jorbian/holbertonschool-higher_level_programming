#!/usr/bin/node

const inputNum = Math.floor(
  Number(
    process.argv[2]
  )
);

function factorial(x) {
  if (x < 1) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

console.log(factorial(inputNum));
