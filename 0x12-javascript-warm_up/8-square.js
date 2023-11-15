#!/usr/bin/node

const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let p = 0; p < size; p++) {
    let row = '';
    for (let q = 0; q < size; q++) row += 'X';
    console.log(row);
  }
}
