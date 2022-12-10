#!/usr/bin/node

const numConv = parseInt(process.argv[2]);

if (numConv) {
  console.log('My number: ' + process.argv[2]);
} else {
  console.log('Not a number');
}
