const fs = require('fs').promises;
const parse = require('csv-parse');

async function countStudents(path) {
  try {
    const fileContent = await fs.readFile(path, 'utf-8');

    const records = await new Promise((resolve, reject) => {
      parse(
        fileContent,
        {
          columns: true,
          skip_empty_lines: true,
        },
        (err, data) => {
          if (err) {
            reject(err);
          } else {
            resolve(data);
          }
        },
      );
    });

    const fieldMap = new Map();

    for (const record of records) {
      const { field } = record;
      const { firstName } = record;

      if (!fieldMap.has(field)) {
        fieldMap.set(field, []);
      }

      fieldMap.get(field).push(firstName);
    }

    console.log(`Number of students: ${records.length}`);

    for (const [field, names] of fieldMap.entries()) {
      console.log(
        `Number of students in ${field}: ${names.length}. List: ${names.join(
          ', ',
        )}`,
      );
    }
  } catch (error) {
    console.error('Cannot load the database');
    throw error;
  }
}

module.exports = countStudents;
