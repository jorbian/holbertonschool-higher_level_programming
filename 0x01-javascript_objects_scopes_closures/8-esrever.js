#!/usr/bin/node

function es (list) {
  return list.reduceRight(function (array, current) {
    array.push(current);
    return array;
  }, []);
}

exports.esrever = es;
