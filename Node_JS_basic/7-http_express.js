const express = require("express");
const fs = require("fs").promises;
const parse = require("csv-parse");

const app = express();

app.listen(1245, () => {
  console.log("Server is running at http://localhost:1245");
});

app.get("/", (req, res) => {
  res.status(200).send("Hello Holberton School!");
});

app.get("/students", async (req, res) => {
  const dbPath = "path-to-database.csv";

  try {
    const fileContent = await fs.readFile(dbPath, "utf-8");

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
        }
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

    const totalStudents = records.length;
    let response = `This is the list of our students\nNumber of students: ${totalStudents}\n`;

    for (const [field, names] of fieldMap.entries()) {
      response += `Number of students in ${field}: ${
        names.length
      }. List: ${names.join(", ")}\n`;
    }

    res.status(200).send(response);
  } catch (error) {
    res.status(500).send("Cannot load the database");
  }
});

module.exports = app;
