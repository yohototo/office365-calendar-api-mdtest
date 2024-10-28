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

// 求模
function modulus(a, b) {
    return a % b;
}

// 指数
function power(a, b) {
    return Math.pow(a, b);
}

// 平方根
function sqrt(a) {
    if (a < 0) {
        throw new Error("Square root of negative number is not allowed.");
    }
    return Math.sqrt(a);
}
// 示例用法
const num1 = 10;
const num2 = 5;

console.log(`加法结果：${add(num1, num2)}`);
console.log(`减法结果：${subtract(num1, num2)}`);
console.log(`乘法结果：${multiply(num1, num2)}`);
console.log(`除法结果：${divide(num1, num2)}`);
console.log(`求模结果：${modulus(num1, num2)}`);
console.log(`指数结果：${power(num1, num2)}`);
