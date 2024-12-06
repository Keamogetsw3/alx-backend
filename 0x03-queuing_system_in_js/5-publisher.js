#!/usr/bin/node

import { createClient } from 'redis';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    redisClient.publish('ALX channel', message);
  }, time);
}

// Call publishMessage as per the requirement
publishMessage("ALX Student #1 starts course", 100);
publishMessage("ALX Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("ALX Student #3 starts course", 400);
