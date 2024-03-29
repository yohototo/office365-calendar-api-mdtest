function add(a, b) {
    return a + b;
}

function subtract(a, b) {
    return a - b;
}
console.log(add(1, 2)); // 输出 3
console.log(subtract(5, 3)); // 输出 2

// calculate.js

// 加法
function add(a, b) {
    return a + b;
}

// 减法
function subtract(a, b) {
    return a - b;
}

// 乘法
function multiply(a, b) {
    return a * b;
}

// 除法
function divide(a, b) {
    if (b === 0) {
        throw new Error("Division by zero is not allowed.");
    }
    return a / b;
}

// 示例用法
const num1 = 10;
const num2 = 5;

console.log(`加法结果：${add(num1, num2)}`);
console.log(`减法结果：${subtract(num1, num2)}`);
console.log(`乘法结果：${multiply(num1, num2)}`);
console.log(`除法结果：${divide(num1, num2)}`);

