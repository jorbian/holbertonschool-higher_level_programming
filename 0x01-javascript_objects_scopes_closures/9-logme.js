#!/usr/bin/node

let count = 0;

function logM (item) {
    console.log(`${count++}: ${item}`);
};

exports.logMe= logM;