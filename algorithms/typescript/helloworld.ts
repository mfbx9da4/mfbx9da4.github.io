type x<Property extends string> = { [K in Property]: K }

let x = <props extends string>(...p: props[]): x<props> => {
  let result = {} as x<props>
  for (let k of p) {
    result[k] = k
  }
  return result
}

let a = x('name', 'age') // Type is x<"name">
console.log(a)
