console.log('hey');
function fib(nth) {
    var arr = [1, 2];
    var i = 3;
    while (i !== nth) {
        arr.push(arr[i - 2] + arr[i - 1]);
        i += 1;
    }
    return arr[array.length - 1];
}
// function indexOfSorted(value, array) {
//   let lo = 0
//   let hi = array.length
//   return _indexOfSorted(array, value, lo, hi)
// }
// let array = [6, 13, 14, 25, 33, 43, 51, 53, 64, 72, 84, 93, 95, 96, 97]
// function _indexOfSorted(array, value, lo, hi) {
//   if (lo >= hi) return -1
//   const mid = Math.floor((hi - lo) / 2) + lo
//   const guess = array[mid]
//   if (array[lo] === value) return lo
//   if (array[hi] === value) return hi
//   if (guess === value) return mid
//   if (value < guess) {
//     hi = mid
//     return _indexOfSorted(array, value, lo, hi)
//   } else {
//     lo = mid + 1
//     return _indexOfSorted(array, value, lo, hi)
//   }
// }
function indexOfSorted(value, array) {
    var lo = 0;
    var hi = array.length;
    while (hi > lo) {
        var mid = Math.floor((hi - lo) / 2) + lo;
        if (array[mid] === value)
            return mid;
        if (value < array[mid]) {
            hi = mid;
        }
        else {
            lo = mid + 1;
        }
    }
    return -1;
}
var array = [6, 13, 14, 25, 33, 43, 51, 53, 64, 72, 84, 93, 95, 96, 97];
console.log(indexOfSorted(95, array));
//# sourceMappingURL=main.js.map