#!/usr/bin/node

const request = require('request');
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(endpoint, function (err, rep, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
