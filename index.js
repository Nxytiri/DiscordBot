const express = require('express');
const noblox = require('noblox.js');
const dotenv = require('dotenv');
const app = express();
const PORT = process.env.PORT || 3000;

dotenv.config();
app.use(express.json());

const GROUP_ID = 32486908;
const AUTH_KEY = process.env.RANK_API_KEY;

(async () => {
  try {
    await noblox.setCookie(process.env.ROBLOX_COOKIE);
    console.log("Logged in to Roblox!");
  } catch (err) {
    console.error("Login failed:", err);
  }
})();

app.post('/rank', async (req, res) => {
  const { username, rank } = req.body;
  const auth = req.headers.authorization;

  if (!auth || auth !== `Bearer ${AUTH_KEY}`) {
    return res.status(403).send("Unauthorized");
  }

  try {
    const userId = await noblox.getIdFromUsername(username);
    const roles = await noblox.getRoles(GROUP_ID);
    const role = roles.find(r => r.name.toLowerCase() === rank.toLowerCase());

    if (!role) return res.status(404).send("Rank not found");

    await noblox.setRank(GROUP_ID, userId, role.rank);
    res.send("User ranked successfully");
  } catch (err) {
    res.status(500).send("Error: " + err.message);
  }
});

app.listen(PORT, () => console.log(`API running on port ${PORT}`));
