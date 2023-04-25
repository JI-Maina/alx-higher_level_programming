#!/usr/bin/node
/* gets the contents of a webpage and stores it in a file */

const request = require('request');
const fs = require('fs');

const file = process.argv[3];
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, (err) => {
      if (err) console.log(err);
    });
  }
});
