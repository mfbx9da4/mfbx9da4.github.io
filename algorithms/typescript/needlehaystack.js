"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const assert_1 = require("./assert");
function strStr(haystack, needle) {
    for (let i = 0; i < haystack.length; i++) {
        if (needle === haystack.substr(i, needle.length)) {
            return i;
        }
    }
    return -1;
}
assert_1.assert(strStr('hello world', 'llo') === 2, strStr('hello world', 'llo').toString());
//# sourceMappingURL=needlehaystack.js.map