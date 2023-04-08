#!/usr/bin/node

const message = 'C is fun';

const numTimes = Math.floor(
  Number(
    process.argv[2]
  )
);

if (isNaN(numTimes)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numTimes; i++) {
    console.log(message);
  }
}
