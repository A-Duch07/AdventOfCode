"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const fs_1 = __importDefault(require("fs"));
const path_1 = __importDefault(require("path"));
// Get input file path
const inputFilePath = path_1.default.join(__dirname, '..', 'input');
// Read file and parse it
let parsedInput = [];
try {
    const input = fs_1.default.readFileSync(inputFilePath, 'utf8');
    parsedInput = input.split('\n');
}
catch (err) {
    console.log(err);
}
// Process input 
let xPos = 0, depthPos = 0, aim = 0;
for (let data of parsedInput) {
    const splitData = data.split(' ');
    if (splitData.length != 2)
        continue;
    const action = splitData[0];
    const dist = parseInt(splitData[1]);
    if (isNaN(dist))
        continue;
    switch (action) {
        case 'forward':
            xPos += dist;
            depthPos += dist * aim;
            break;
        case 'up':
            aim -= dist;
            break;
        case 'down':
            aim += dist;
            break;
        default:
            break;
    }
}
console.log(xPos * depthPos);
