#!/usr/bin/node
const data = process.argv.splice(2);

if (data.length < 2) {
  console.log('0');
} else {
  data.sort(function (a, b) { return b - a; });
  console.log(data[1]);
}
