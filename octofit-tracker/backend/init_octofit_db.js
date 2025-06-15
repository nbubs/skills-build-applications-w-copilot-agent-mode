use octofit_db;

// Initialize collections and indexes for octofit_db

// Connect to the octofit_db database
db = db.getSiblingDB('octofit_db');

// Create users collection with unique email index
db.createCollection('users');
db.users.createIndex({ "email": 1 }, { unique: true });

// Create teams collection
db.createCollection('teams');

// Create activity collection
db.createCollection('activity');

// Create leaderboard collection
db.createCollection('leaderboard');

// Create workouts collection
db.createCollection('workouts');

show collections;
