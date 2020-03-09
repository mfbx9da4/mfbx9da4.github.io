console.log('start file');
let asdf = {
    asdf: 'asdf',
    asdf2: 'asdf2',
};
console.log(asdf);
function construct(keys) {
    let obj = {};
    for (let k of keys) {
        obj[k] = k;
    }
    return obj;
}
let out = construct(['asdf', 'asdf2']);
console.log('hey');
console.log(out);
//# sourceMappingURL=key_to_key.js.map