import fs from 'fs';

const writeFile = (filePath, data) => {
    fs.writeFile(filePath, JSON.stringify(data, null, 2), "utf8", (err) => {
        if (err) {
            reject(err);
        } else {
            resolve("Item added succesfully");
        }
    });
};

export default writeFile;