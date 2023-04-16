#!/usr/bin/node

const request = require('request');

const endpoint = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(
  endpoint,
  (err, body) => (
    err ? console.log(err) : console.log(JSON.parse(body).title)
  )
);
