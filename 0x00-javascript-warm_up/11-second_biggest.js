#!/usr/bin/node

let numbers = (
  (process.argv).slice(2)
    .map(Number)
);

if (numbers.length < 2) {
  console.log(0);
} else {
  numbers = numbers.map(num => parseInt(num));
  const max = Math.max(...numbers);
  numbers = nums.filter(num => num !== max);
  console.log(Math.max(...numbers));
}
