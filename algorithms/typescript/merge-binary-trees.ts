import { assert } from './assert'

type BinaryTree = {
  left?: BinaryTree
  right?: BinaryTree
  val: number
}

function mergeBinaryTrees(tree1: BinaryTree, tree2: BinaryTree) {
  // traverse both at the same time
  // if one does not have it, just copy from the other
  const newTree: BinaryTree = {
    val: 0,
  }
  const list: Array<[
    BinaryTree,
    BinaryTree | undefined,
    BinaryTree | undefined
  ]> = [[newTree, tree1, tree2]]
  while (list.length) {
    const [c, a, b] = list.pop()
    if (a !== undefined && b !== undefined) {
      c.val = a.val + b.val
      c.left = { val: 0 }
      list.push([c.left, a.left, b.left])
      c.right = { val: 0 }
      list.push([c.right, a.right, b.right])
    } else if (a !== undefined) {
      c.val = a.val
      c.left = a.left
      c.right = a.right
    } else if (b !== undefined) {
      c.val = b.val
      c.left = b.left
      c.right = b.right
    }
  }
  return newTree
}

const a: BinaryTree = {
  val: 1,
  left: {
    val: 1,
    left: {
      val: 3,
    },
  },
}

const b: BinaryTree = {
  val: 1,
  right: {
    val: 1,
  },
}

console.log('mergeBinaryTrees(a, b)', mergeBinaryTrees(a, b))
