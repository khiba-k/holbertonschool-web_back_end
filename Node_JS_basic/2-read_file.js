const fs = require("fs");

function countStudents(database) {
    try {
        fs.createReadStream(database)
    }
    catch(error) {

    }
}

module.exports = countStudents();