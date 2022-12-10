#!/usr/bin/node

const num = Number(process.argv[2]);

function factorial (num) {
  if (!num || num === 0 || num === 1) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}
console.log(factorial(num));
