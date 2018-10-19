
function combinate (setSize, wordSize, prevWord) {
  var i = 0
  var words = []
  while (i < setSize) {
    var word = prevWord.concat()
    word.push(i)
    if (word.length === wordSize) {
      words.push(word)
    } else {
      var childWords = combinate(setSize, wordSize, word)
      words = words.concat(childWords)
    }
    i += 1
  }
  return words
}

function combinateV2 (setSize, wordSize) {
  var queue = []
  for (var i = 0; i < setSize; i ++) queue.push([i])

  var out = []

  while (queue.length) {
    var item = queue.shift()
    if (item.length === wordSize) {
      out.push(item)
      continue
    }
    for (var i = 0; i < setSize; i ++) {
      newItem = item.concat()
      newItem.push(i)
      queue.push(newItem)
    }
  }

  return out
}

function combinateV3 (set1Size, set2Size, wordSize) {
  var queue = []
  for (var i = 0; i < set1Size; i ++) queue.push([i])

  var out = []

  while (queue.length) {
    var item = queue.shift()

    // end of word
    if (item.length === wordSize) {
      out.push(item)
      continue
    }

    // add letter
    var size = item.length % 2 === 0 ? set1Size : set2Size
    for (var i = 0; i < size; i ++) {
      newItem = item.concat()
      newItem.push(i)
      queue.push(newItem)
    }
  }

  return out
}

function print (words) {
  var dict = {
    0: 'ponte',
    1: 'bananeira',
    2: 'cocorinha',
    3: 'negativa'
  }
  var out = []
  for (var i = 0; i < words.length; i ++) {
    var word = words[i]
    var trs = word.map(x => dict[x]).join(' - ')
    console.log(trs)
  }
  return out
}

function print_sequence (words) {
  var positions = {
    0: 'ponte',
    1: 'bananeira',
    2: 'negativa',
    3: 'cocorinha'
  }
  var transitions = {
    0: 'macaco',
    1: 'switch',
    2: 'spin'
  }
  var out = []
  for (var i = 0; i < words.length; i ++) {
    var word = words[i]
    console.log(word)
    var trs = []
    for (let i = 0; i < word.length; i ++) {
      let letter = word[i]
      if (i % 2 === 0) {
        trs.push(positions[letter])
      } else {
        trs.push(transitions[letter])
      }
    }
    trs = trs.join(' - ')
    console.log(trs)
  }
  return out
}

var set1Size = 3
var set2Size = 2
var wordSize = 5
// var ans = combinateV2(setSize, wordSize, [])
// var translatedAns = print(ans)
var ans = combinateV3(set1Size, set2Size, wordSize)
var translatedAns = print_sequence(ans)
console.log('ans.length', ans.length)
// console.log(JSON.stringify(translatedAns, null, 2))
