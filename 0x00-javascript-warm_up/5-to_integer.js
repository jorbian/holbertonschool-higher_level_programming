#!/usr/bin/node

let message;

const argument = Math.floor(
  Number(
    process.argv[2]
  )
);

if (isNaN(argument)) {
  message = 'Not a number';
} else {
  message = `My number: ${Number(argument)}`;
}

console.log(message);
