#!/usr/bin/node

function numOfOccurances (list, searchElement) {
  return list.reduce(
    (count, current) => current === searchElement ? count + 1 : count, 0
  );
}

exports.nbOccurences = numOfOccurances;
