import { createClient, print } from 'redis';

const redisClient = createClient();

redisClient.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
  redisClient.SET(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
  redisClient.GET(schoolName, (_err, reply) => {
    console.log(reply);
  });
};

displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});
