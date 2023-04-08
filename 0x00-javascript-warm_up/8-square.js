#!/usr/bin/node

const area = Math.floor(
  Number(
    process.argv[2]
  )
);

if (!isNaN(area)) {
  let square = '';
  const block = 'X';

  for (let i = 0; i < area; i++) {
    for (let j = 0; j < area; j++) {
      square += block;
    }
    square = (i == area) ? square: square + '\n';
  }

  console.log(square);
} else {
  console.log('Missing size');
}
