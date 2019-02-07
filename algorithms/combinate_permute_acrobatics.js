// Every unqiue sequence will start with one
// of the following positions
// Start with the first position as our base
// Sequence
[[P ...], [N ... ], [C ... ], [B ...]]
// How do we extend the sequence by one position?
// => Add a position not already in the sequence
[P, N]
[P, C]
[P, B]
// How do we know we have a full sequence?
// => sequence of length 4 or all positions used
[P, N, C, B]

function generateSequences (nMovements, sequenceLength) {
  var openList = []
  for (let i = 0; i < nMovements; i ++) {
    openList.push([i])
  }

  var sequences = []
  while (openList.length) {
    var partSequence = openList.pop()
    if (partSequence.length === sequenceLength) {
      sequences.push(partSequence)
      continue
    }
    var movementsInThisSequence = new Set(partSequence)
    for (let i = 0; i < nMovements; i ++) {
      if (!movementsInThisSequence.has(i)) {
        newSequence = partSequence.concat()
        newSequence.push(i)
        openList.push(newSequence)
      }
    }
  }
}











































function combinateRecursive (setSize, sequenceSize, prevWord) {
  var i = 0
  var words = []
  while (i < setSize) {
    var word = prevWord.concat()
    word.push(i)
    if (word.length === sequenceSize) {
      words.push(word)
    } else {
      var childWords = combinateRecursive(setSize, sequenceSize, word)
      words = words.concat(childWords)
    }
    i += 1
  }
  return words
}

function combinate (setSize, sequenceSize, canRepeat) {
  var queue = []
  for (var i = 0; i < setSize; i ++) queue.push([i])

  var out = []

  while (queue.length) {
    var item = queue.shift()

    // if full sequence
    if (item.length === sequenceSize) {
      out.push(item)
      continue
    }

    // add a permutation increasing word size by one
    var existingItems = !canRepeat && new Set(item)
    for (var i = 0; i < setSize; i ++) {
      if (canRepeat || !existingItems.has(i)) {
        newItem = item.concat()
        newItem.push(i)
        queue.push(newItem)
      }
    }
  }

  return out
}

function combinateWithTranstions (set1Size, set2Size, sequenceSize) {
  var queue = []
  for (var i = 0; i < set1Size; i ++) queue.push([i])

  var out = []

  while (queue.length) {
    var item = queue.shift()

    // end of word
    if (item.length === sequenceSize) {
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
    2: 'qdr',
    3: 'cocorinha',
    4: 'negativa'
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
    1: 'QDR',
    2: 'bananeira',
    3: 'cocorinha'
  }
  var transitions = {
    0: 'flip',
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

var setSize = 4
var sequenceSize = 4
var ans = combinate(setSize, sequenceSize, false)
var translatedAns = print(ans)
console.log(ans.length, 4**4, 4 * 3 * 2 * 1)

var set1Size = setSize
var set2Size = 2
sequenceSize = 5
// var ans = combinateWithTranstions(set1Size, set2Size, sequenceSize)
// var translatedAns = print_sequence(ans)
// console.log(JSON.stringify(translatedAns, null, 2))
