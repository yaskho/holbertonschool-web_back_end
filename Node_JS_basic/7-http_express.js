const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const databaseFile = process.argv[2]; // Get CSV file from command-line argument

// Root endpoint
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// /students endpoint
app.get('/students', async (req, res) => {
  let output = 'This is the list of our students\n';

  try {
    await countStudents(databaseFile, (msg) => {
      output += msg; // Append the result of countStudents to output
    });
    res.send(output);
  } catch (error) {
    res.send('Cannot load the database');
  }
});

// Listen on port 1245
app.listen(1245);

module.exports = app;
