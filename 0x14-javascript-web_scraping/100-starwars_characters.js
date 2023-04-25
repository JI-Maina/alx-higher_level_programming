#!/usr/bin/node
/* prints all characters of a Star Wars movie */

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

// film details by id
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;

    // grab character details
    for (const character of characters) {
      request(character, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const person = JSON.parse(body);
          console.log(person.name);
        }
      });
    }
  }
});
