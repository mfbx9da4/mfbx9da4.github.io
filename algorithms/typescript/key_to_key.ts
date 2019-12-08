console.log('start file')
type KeyToKey<Property extends string> = { [K in Property]: K }

let asdf: KeyToKey<'asdf' | 'asdf2'> = {
  asdf: 'asdf',
  asdf2: 'asdf2',
}
console.log(asdf)

function construct<Key extends string>(keys: Key[]): KeyToKey<Key> {
  let obj = {} as KeyToKey<Key>
  for (let k of keys) {
    obj[k] = k
  }
  return obj
}
let out = construct(['asdf', 'asdf2'])
console.log('hey')
console.log(out)
