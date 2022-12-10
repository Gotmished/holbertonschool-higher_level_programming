#!/usr/bin/node

const data = process.argv.splice(2);

if (data.length === 0 || data.length === 1) {
  console.log('0');
} else {
  data.sort();
  console.log(data[data.length - 2]);
}
