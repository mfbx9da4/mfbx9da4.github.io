// function mergeSort(array: Array<number>) {
//   if (array.length === 1) return array
//   if (array.length === 2) {
//     if (array[0] > array[1]) return [array[1], array[0]]
//     return array
//   }
//   const mid = Math.floor(array.length / 2)
//   const left = mergeSort(array.slice(0, mid))
//   const right = mergeSort(array.slice(mid))
//   return left.concat(right)
// }

function mergeSort(array: Array<number>) {
  if (array.length === 1) return array
  if (array.length === 2) {
    if (array[0] > array[1]) return [array[1], array[0]]
    return array
  }
  const mid = Math.floor(array.length / 2)
  const left = mergeSort(array.slice(0, mid))
  const right = mergeSort(array.slice(mid))
  return left.concat(right)
}

function generateNumbers(num: number = 8): Array<number> {
  const out: Array<number> = []
  for (let i = 0; i < num; i++) {
    out.push(Math.floor(Math.random() * 100))
  }
  return out
}

console.log(generateNumbers())
