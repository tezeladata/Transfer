const express = require("express");

const app = express();

app.get("/", (req, res) => {
    let newItem = JSON.stringify([
        {name: "a", number: 1},
        {name: "b", number: 2},
        {name: "c", number: 3},
    ]);

    console.log(newItem);
    res.send(newItem)
})

let accounts = [];

app.post("/accounts", (req, res) => {
    let body = "";

    req.on("data", (chunk) => {
        body += chunk;
    })

    req.on("end", () => {
        accounts.push(body);

        console.log(`Account added \n${accounts}`);
        res.send(JSON.stringify(accounts));
    })
})

app.delete("/accounts", (req, res) => {
    accounts.pop();

    console.log(`Last account removed \n${accounts}`)
    res.send(JSON.stringify(accounts))
})

app.listen(5050, () => console.log("Server started on port 5050"))