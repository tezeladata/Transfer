const fs = require("fs");
const readline = require("readline");

const interface1 = readline.createInterface({
    input: fs.createReadStream("data.txt")
})

let lineNumber = 1
interface1.on("line", (fileline) => {
    console.log(`Line N${lineNumber}: ${fileline}`)
    lineNumber++;
})