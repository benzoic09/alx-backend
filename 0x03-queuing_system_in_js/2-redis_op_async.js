import { createClient, print } from 'redis';
import { promisify } from 'util'

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// promisefy the client.get
const getAsync  = promisify(client.get).bind(client)

// function to set a new value 
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

// function to display
async function displaySchoolValue(schoolName) {
    try {
        const reply = await getAsync(schoolName);
        console.log(reply);
    } catch (err) {
        console.log(`Error retrieving value for ${schoolName}: ${err.message}`);
    }
    
}

// Call the functions as specified
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');