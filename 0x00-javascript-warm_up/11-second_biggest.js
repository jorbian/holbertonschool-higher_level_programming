#!/usr/bin/node

const numbers = (
  (process.argv).slice(2)
    .map(Number)
);

if (numbers.length <= 1) {
  console.log(0);
} else {
  console.log(
    numbers.sort()[numbers.length - 2]
  );
}
