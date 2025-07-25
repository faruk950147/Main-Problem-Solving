let str = "Hello, World!";
let regexp = /World/;
console.log(regexp.test(str));  // true

let str1 = "Hello, World!";
let regexp1 = /World/;
console.log(regexp1.exec(str1));  // ["World", index: 7, input: "Hello, World!", groups: undefined]
