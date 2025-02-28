// 绝对值
function absolute(a) {
    return Math.abs(a);
}

// 阶乘
function factorial(n) {
    if (n < 0 || !Number.isInteger(n)) {
        throw new Error("Factorial is only defined for non-negative integers.");
    }
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

// 最大公约数（GCD）
function gcd(a, b) {
    a = Math.abs(a);
    b = Math.abs(b);
    while (b !== 0) {
        [a, b] = [b, a % b];
    }
    return a;
}

// 最小公倍数（LCM）
function lcm(a, b) {
    if (a === 0 || b === 0) {
        return 0;
    }
    return Math.abs(a * b) / gcd(a, b);
}

// 随机数生成
function randomInRange(min, max) {
    if (min > max) {
        throw new Error("Minimum value cannot be greater than maximum value.");
    }
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// 数组求和
function sumArray(arr) {
    if (!Array.isArray(arr)) {
        throw new Error("Input must be an array.");
    }
    return arr.reduce((sum, num) => sum + num, 0);
}

// 数组平均值
function averageArray(arr) {
    if (!Array.isArray(arr) || arr.length === 0) {
        throw new Error("Input must be a non-empty array.");
    }
    return sumArray(arr) / arr.length;
}

// 示例用法
console.log(`绝对值结果：${absolute(-15)}`);
console.log(`阶乘结果：${factorial(5)}`);
console.log(`最大公约数结果：${gcd(48, 18)}`);
console.log(`最小公倍数结果：${lcm(12, 15)}`);
console.log(`随机数结果（1到100）：${randomInRange(1, 100)}`);

const numbers = [1, 2, 3, 4, 5];
console.log(`数组求和结果：${sumArray(numbers)}`);
console.log(`数组平均值结果：${averageArray(numbers)}`);
