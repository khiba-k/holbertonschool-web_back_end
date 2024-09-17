const fs = require("fs");

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, "utf8");

    const lines = data.split("\n");

    const validLines = lines.filter((line) => line.trim() !== "");

    if (validLines.length <= 1) {
      throw new Error("Cannot load the database");
    }

    console.log(`Number of students: ${validLines.length - 1}`);

    const fields = {};

    for (let i = 1; i < validLines.length; i++) {
      const studentInfo = validLines[i].split(",");

      if (studentInfo.length >= 4) {
        const firstName = studentInfo[0];
        const field = studentInfo[3];

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      }
    }

    for (const field in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, field)) {
        const list = fields[field].join(", ");
        console.log(
          `Number of students in ${field}: ${fields[field].length}. List: ${list}`
        );
      }
    }
  } catch (error) {
    throw new Error("Cannot load the database");
  }
}

module.exports = countStudents;
