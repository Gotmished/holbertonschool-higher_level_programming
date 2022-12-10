#!/usr/bin/node
const data = process.argv.splice(2);

if (data.length < 2) {
  console.log('0');
} else {
  data.reverse();
  console.log(data[1]);
}
