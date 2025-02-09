import express from "express";
import { dirname } from "path";
import { fileURLToPath } from "url";
import readFile from "../Utils/readFile.js";

const __dirname = dirname(fileURLToPath(import.meta.url));
const filePath = `${__dirname}/../Databases/mentors.json`;

export const MentorsRoute = express.Router();

MentorsRoute.get("/", async (req, res) => {
    const {limit, sort} = req.query;
    try {
        let mentors = await readFile(filePath);

        // limit query
        if (limit) {
            mentors = mentors.slice(0, parseInt(limit));
        }

        // sort query
        if (sort) {
            switch (sort.toLowerCase()) {
                case "asc":
                    mentors.sort((a, b) => a.mentor.localeCompare(b.mentor));
                    break;
                case "desc":
                    mentors.sort((a, b) => b.mentor.localeCompare(a.mentor));
                    break;
            }
        }

        res.status(200).json(mentors);
    } catch (e) {
        console.error("Error reading database:", e);
        return res.status(500).send("Database could not be read");
    }
});

MentorsRoute.get("/:id", async (req, res) => {
    const id = req.params.id;
    try {
        const mentors = await readFile(filePath);
        
        // find mentor
        const result = mentors.filter(mentor => mentor.mentor === id);

        res.json(result)
    } catch(e) {
        console.error(e);
        return res.status(500).send("Database could not be read")
    }
})