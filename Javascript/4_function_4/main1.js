function test(){
    for (let i = 0; i < arguments.length; i++) {
        console.log(arguments[i]);
    }
}
test(1,2,3,4,5);


function add(){
    sum = 0;
    for (let i = 0; i < arguments.length; i++) {
        sum += arguments[i];
    }
    return sum;
}
console.log(add(1,2,3,4,5));