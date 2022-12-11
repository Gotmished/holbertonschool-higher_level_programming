#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }
  return count;
};

// #!/usr/bin/node
// exports.nbOccurences = function (list, searchElement) {
//  let count = 0;
//  for (const eachItem of list) {
//    if (eachItem === searchElement) {
//      count += 1;
//    }
//  }
//  return count;
// };
