#!/usr/bin/node
/* computes the number of tasks completed by user id */

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const userIds = [];
    const todos = JSON.parse(body);

    // grab all the user ids
    for (const todo of todos) {
      if (!userIds.includes(todo.userId)) {
        userIds.push(todo.userId);
      }
    }

    const compTask = {};

    // compute completed tasks and update obj
    for (const id of userIds) {
      let count = 0;
      for (const todo of todos) {
        if (todo.userId === id) {
          if (todo.completed) {
            count += 1;
          }
        }
        if (count !== 0) compTask[id] = count;
      }
    }
    console.log(compTask);
  }
});
