#!/usr/bin/node
/* writes a string to a file in utf-8 */

const fs = require('fs');
const path = process.argv[2];
const text = process.argv[3];

fs.writeFile(path, text, (err) => {
  if (err) console.log(err);
});
