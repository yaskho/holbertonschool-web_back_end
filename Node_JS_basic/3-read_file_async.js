const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split(/\r?\n/).filter((l) => l.trim() !== '');

      if (lines.length <= 1) {
        console.log('Number of students: 0');
        resolve();
        return;
      }

      lines.shift();

      const fields = new Map();
      let total = 0;

      for (const line of lines) {
        const parts = line.split(',');
        if (parts.length < 4) continue;

        const firstName = parts[0].trim();
        const field = parts[3].trim();
        if (!firstName || !field) continue;

        total += 1;

        if (!fields.has(field)) {
          fields.set(field, []);
        }
        fields.get(field).push(firstName);
      }

      console.log(`Number of students: ${total}`);
      for (const [field, names] of fields.entries()) {
        console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }

      resolve();
    });
  });
}

module.exports = countStudents;
