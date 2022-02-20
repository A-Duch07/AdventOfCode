import fs from 'fs';
import path from 'path';

// Get input file path
const inputFilePath: string = path.join(__dirname, '..', 'input');

// Read file and parse it
let parsedInput: string[] = [];
try {
    const input: string = fs.readFileSync(inputFilePath, 'utf8');
    parsedInput = input.split('\n');
} catch (err) {
    console.log(err)
}

// Process input 
let xPos: number = 0,
    depthPos: number = 0,
    aim: number = 0;

for (let data of parsedInput) {
    const splitData: string[] = data.split(' ')

    if (splitData.length != 2) continue;

    const action: string = splitData[0]
    const dist: number = parseInt(splitData[1])

    if(isNaN(dist)) continue;

    switch(action) {
        case 'forward':
            xPos += dist;
            depthPos += dist * aim;
            break;
        case 'up' :
            aim -= dist;
            break;
        case 'down':
            aim += dist;
            break;
        default: 
            break;
    }
}

console.log(xPos * depthPos)