import express from "express";
import { dirname } from "path";
import { fileURLToPath } from "url";
import readFile from "../Utils/readFile.js";

const __dirname = dirname(fileURLToPath(import.meta.url));
const filePath = `${__dirname}/../Databases/leaders.json`;

export const LeadersRoute = express.Router();

LeadersRoute.get("/", async (req, res) => {
    const {limit, sort} = req.query;

    try {
        let leaders = await readFile(filePath);

        // limit query
        if (limit) {
            leaders = leaders.slice(0, parseInt(limit));
        }

        // sort query
        if (sort) {
            switch (sort.toLowerCase()) {
                case "asc":
                    leaders.sort((a, b) => a.Salary - b.Salary);
                    break;
                case "desc":
                    leaders.sort((a, b) => b.Salary - a.Salary);
                    break;
            }
        }

        res.status(200).json(leaders)
    } catch(e) {
        console.error(e);
        return res.status(500).json("Failed to read database")
    }
})

LeadersRoute.get("/salary", async (req, res) => {
    const {limit, sort} = req.query;

    try {
        let all = await readFile(filePath);
        let leaders = all.map(leader => ({"Leader": leader.Leader, "Salary": leader.Salary}));

        // limit query
        if (limit) {
            leaders = leaders.slice(0, parseInt(limit));
        }

        // sort query
        if (sort) {
            switch (sort.toLowerCase()) {
                case "asc":
                    leaders.sort((a, b) => a.Salary - b.Salary);
                    break;
                case "desc":
                    leaders.sort((a, b) => b.Salary - a.Salary);
                    break;
            }
        };

        res.status(200).json(leaders);
    } catch(e) {
        console.error(e);
        return res.status(500).json("Could not read database")
    }
})

LeadersRoute.get("/members", async (req, res) => {
    const {sort, limit} = req.query;

    try {
        let all = await readFile(filePath);
        let leaders = all.map(leader => ({"Leader": leader.Leader, "member count": leader["member count"]}));

        // limit query
        if (limit) {
            leaders = leaders.slice(0, parseInt(limit));
        }

        // sort query
        if (sort) {
            switch (sort.toLowerCase()) {
                case "asc":
                    leaders.sort((a, b) => a["member count"] - b["member count"]);
                    break;
                case "desc":
                    leaders.sort((a, b) => b["member count"] - a["member count"]);
                    break;
            }
        };

        res.status(200).json(leaders);
    } catch(e) {
        console.error(e);
        res.status(500).json("Could not read database")
    }
})

LeadersRoute.get("/:id", async (req, res) => {
    const id = req.params.id;

    try {
        let leaders = await readFile(filePath);
        const leader = leaders.filter(a => a.Leader === id);

        if (leader.length === 0){
            return res.status(404).json("Leader not found")
        }

        res.status(200).json(leader)
    } catch(e) {
        console.error(e);
        return res.status(500).json("Failed to read database")
    }
})