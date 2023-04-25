#!/usr/bin/node
/* prints the number of movies where the character “Wedge Antilles” is present */

const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    for (const film of films) {
      const characters = film.characters;
      for (const character of characters) {
        if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
          count = count + 1;
        }
      }
    }
    console.log(count);
  }
});
