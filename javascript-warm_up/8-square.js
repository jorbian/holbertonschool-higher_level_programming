#!/usr/bin/node

const area = Math.floor(
  Number(
    process.argv[2]
  )
);

if (!isNaN(area)) {
  const block = 'X';

  for (let r = 0; r < area; r++) {
    let row = '';
    for (let c = 0; c < area; c++) row += block;
    console.log(row);
  }
} else {
  console.log('Missing size');
}
