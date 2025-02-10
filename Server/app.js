import express from "express"
import cors from "cors"
import { MentorsRoute } from "./Routers/mentors.route.js";
import { LeadersRoute } from "./Routers/leaders.route.js";

const app = express();

app.use(cors());
app.use(express.json());

// Routers
app.use("/mentors", MentorsRoute);
app.use("/leaders", LeadersRoute);

app.listen(3000, () => console.log("Server started on port 3000"))