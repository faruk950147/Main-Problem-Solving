// str1 = "Hello World!"
// console.log(str1.length)
// let length = 0;

// while (true) {
//     if (str1.charAt(length) == "") {
//         break;
//     }
//     length++;
// }
// console.log(length);

arr = [1, 2, 3, 4, 5];
console.log(arr.length); // Output: 5

// let Length = 0;

// while (arr[Length] !== undefined) {
//     Length++;
// }
// console.log(Length); // Output: 5

// for (let i = 0; i < arr.length; i++) {
//     console.log(arr[i]);
//     arr[i] = arr[i] * 2;
// }
// console.log(arr);
sum = 0;    
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
    sum += arr[i];
}
console.log(sum);

