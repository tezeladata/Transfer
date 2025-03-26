import express from "express";
import readFile from "../Utils/readFile.js";
import writeFile from "../Utils/writeFile.js";

// Route
export const todo = express.Router();

// database
const filepath = "./Database/todos.json"

// get all tasks
todo.get("/", async (req, res) => {
    const { limit, status, priority } = req.query;
    try {
        // Get data
        let data = await readFile(filepath);

        // queries
        if (limit) {
            if (limit < 0) {
                return res.status(404).send("Limit should be non-negative number")
            }
            if (limit > data.length) {
                return res.status(404).send("Limit is higher than the count of elements")
            }
            data = data.splice(0, parseInt(limit))
        }

        if (status) {
            switch (status) {
                case "completed":
                    data = data.filter(item => item.status === "completed");
                    if (data.length === 0) {
                        return res.status(404).send("No tasks are completed");
                    }
                    break;
                case "in-progress":
                    data = data.filter(item => item.status === "in-progress");
                    if (data.length === 0) {
                        return res.status(404).send("No tasks are in-progress");
                    }
                    break;
                default:
                    return res.status(404).send("Wrong value for query named status");
            }
        }

        if (priority) {
            if (priority) {
                switch (priority) {
                    case "low":
                        data = data.filter(item => item.priority === "low");
                        break;
                    case "normal":
                        data = data.filter(item => item.priority === "normal");
                        break;
                    case "high":
                        data = data.filter(item => item.priority === "high");
                        break;
                    default:
                        return res.status(404).send("Wrong value for query named priority");
                }
            }
        }
        
        // Send tasks
        res.status(200).json(data)
    } catch (e) {
        return res.status(400).send("Database could not be read")
    }
})