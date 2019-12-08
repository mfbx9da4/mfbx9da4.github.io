let x = (...p) => {
    let result = {};
    for (let k of p) {
        result[k] = k;
    }
    return result;
};
let a = x('name', 'age'); // Type is x<"name">
console.log(a);
//# sourceMappingURL=helloworld.js.map