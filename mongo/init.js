const crypto = require("crypto");

const app = db.getSiblingDB('app');
app.users.insertOne({ user: "admin", pass: crypto.randomBytes(64).toString("hex") });

const secret = db.getSiblingDB('secret');
secret.flag.insertOne({ flag: process.env.FLAG || "W1{nice_try_without_gopher}" });
