#!/usr/bin/node

exports.esrever = function (list) {
  const data = [];
  while (list.length) {
    data.push(list.pop());
  }
  return data;
};
