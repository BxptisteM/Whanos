const fs = require('fs');
const Befunge = require('befunge93');

const programFile = process.argv[2];

if (!programFile) {
    console.error("Usage: node interpreter.js <program.bf>");
    process.exit(1);
}

fs.readFile(programFile, 'utf8', (err, data) => {
    if (err) {
        console.error("Error while reading file:", err.message);
        process.exit(1);
    }

    let befunge = new Befunge();

    befunge.run(data.trim())
        .then(output => {
            process.stdout.write(output);
        })
        .catch(err => {
            console.error("Error running program:", err.message);
        });
});
