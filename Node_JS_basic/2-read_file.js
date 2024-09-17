const fs = require("fs");

function countStudents(database) {
    try {
        const data = fs.readFileSync(database, 'utf-8');
        const lines = data.split('\n').filter(line => line.trim().length > 0);
        if (lines.length <= 1) {
            throw new Error("Cannot load the database");
        }

        const fields = {};
        lines.slice(1).forEach((line) => {
            const [firstName, , field] = line.split(',');
            if (fields[field]) {
                fields[field].push(firstName);
            } else {
                fields[field] = [firstName];
            }
        });

        console.log(`Number of students: ${lines.length - 1}`);
        for (const [field, students] of Object.entries(fields)) {
            console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
        }
    } catch (error) {
        throw new Error("Cannot load the database");
    }
}

module.exports = countStudents;
