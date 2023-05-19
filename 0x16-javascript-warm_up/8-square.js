#!/usr/bin/node

const numConv = parseInt(process.argv[2]);
let i, j;

if (numConv) {
  for (i = 0; i < process.argv[2]; i++) {
    let row = '';
    for (j = 0; j < process.argv[2]; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
