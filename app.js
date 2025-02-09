import express from "express"
import cors from "cors"
import { MentorsRoute } from "./Routers/mentors.route.js";

const app = express();

app.use(cors());
app.use(express.json());

// Routers
app.use("/mentors", MentorsRoute)

app.listen(3000, () => console.log("Server started on port 3000"))