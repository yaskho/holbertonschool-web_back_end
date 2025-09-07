const fs = require('fs');

function countStudents(path) {
  if (!fs.existsSync(path)) {
    throw new Error('Cannot load the database');
  }

  let data;
  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = data.split(/\r?\n/).filter((l) => l.trim() !== '');

  if (lines.length === 0) {
    console.log('Number of students: 0');
    return;
  }

  const header = lines.shift();

  const fields = new Map();
  let totalStudents = 0;

  for (const line of lines) {
    const parts = line.split(',');
    if (parts.length < 4) continue;

    const firstName = parts[0].trim();
    const field = parts[3].trim();

    if (!firstName || !field) continue;

    totalStudents += 1;

    if (!fields.has(field)) {
      fields.set(field, []);
    }
    fields.get(field).push(firstName);
  }

  console.log(`Number of students: ${totalStudents}`);
  for (const [field, names] of fields.entries()) {
    console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
  }
}

module.exports = countStudents;
