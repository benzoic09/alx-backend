import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});


// function to set a new value 
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

// function to display
function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.error(`Error retrieving value for ${schoolName}: ${err.message}`);
        } else {
            console.log(reply);
        }
    });
}

// Call the functions as specified
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');