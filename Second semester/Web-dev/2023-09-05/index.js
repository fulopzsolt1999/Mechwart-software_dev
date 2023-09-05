/* Pop up windows */
const getNum = prompt("Give me a number: ");
/* alert("Hello world!"); */

/* Global variable declaration */
var c;
/* Local variable declaration */
let a;
/* Constans variable declaration */
const b = 0;

/* Write to the web page */
document.write("<h1>Hello world</h1>");

/* Fibonacci number generator */
/* let x = [];
let y = 0;
for (let i = 0; i < 30; i++) {
    if (i < 2) {
        x.push(1);
    } else {
        x.push(x[y]+x[y+1]);
        y += 1;
    }
}
document.write("<table>");
for (let j = 0; j < x.length; j++) {
    document.write("<tr><td>" + x[j] + "</td></tr>");
}
document.write("</table>"); */

/* Dice rolling */
let randomNums = [];
let diceNums = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0
};
for (let i = 0; i < getNum; i++) {
    let randNum = Math.floor(Math.random() * 6) + 1;
    if (randNum == 1) {
      diceNums["1"] += 1;
    } else if (randNum == 2) {
      diceNums["2"] += 1;
    } else if (randNum == 3) {
      diceNums["3"] += 1;
    } else if (randNum == 4) {
      diceNums["4"] += 1;
    } else if (randNum == 5) {
      diceNums["5"] += 1;
    } else {
      diceNums["6"] += 1;
    }
}
document.write("<table>");
for (let x in diceNums) {
    document.write("<tr><td>" + x + ": " + diceNums[x] + "<br>előfordulás: " + diceNums[x] / getNum * 100 + "%" +"</td></tr>");
}
document.write("</table>");