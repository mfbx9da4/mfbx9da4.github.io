class MinHeap {
  private values: Array<number> = []

  push(...x) {
    for (const val of x) {
      this.values.push(val)
      this.percolate(this.values.length - 1)
    }
  }

  private getParent(i: number): [number, number] {
    if (i === 0) throw new Error('Root has no parent')
    //      [0, 1, 2, 3, 4, 5, 6, 7, 8]
    //                    0
    //            1               2
    //         3      4       5       6
    //       7   8   9 10   11 12   13 14
    const index = Math.round(i / 2) - 1
    return [index, this.values[index]]
  }

  private getChildren(i: number): [number, number, number, number] {
    let a = i * 2 + 1
    let b = i * 2 + 2
    return [a, this.values[a], b, this.values[b]]
  }

  private percolate(index: number) {
    if (index === 0) return
    const [parentIndex, parent] = this.getParent(index)
    if (parent === undefined || this.values[index] < parent) {
      this.swap(index, parentIndex)
      this.percolate(parentIndex)
    }
  }

  private swap(i, j) {
    const temp = this.values[i]
    this.values[i] = this.values[j]
    this.values[j] = temp
  }

  private sink(i: number) {
    const val =
      this.values[i] === undefined ? Number.POSITIVE_INFINITY : this.values[i]
    const [leftIndex, left, rightIndex, right] = this.getChildren(i)

    if (left !== undefined && right !== undefined) {
      const min = Math.min(left, right, val)
      if (min === left) {
        this.swap(i, leftIndex)
        this.sink(leftIndex)
      } else if (min === right) {
        this.swap(i, rightIndex)
        this.sink(rightIndex)
      }
    } else if (left !== undefined && left < val) {
      this.swap(i, leftIndex)
      this.sink(leftIndex)
    } else if (right !== undefined && right < val) {
      this.swap(i, rightIndex)
      this.sink(rightIndex)
    }

    while (
      this.values.length > 0 &&
      this.values[this.values.length - 1] === undefined
    ) {
      this.values.pop()
    }
  }

  log() {
    console.log('this.values', this.values)
  }

  pop(): number {
    this.log()
    const min = this.values[0]
    this.values[0] = undefined
    this.sink(0)
    return min
  }

  top(): number {
    return this.values[this.values.length - 1]
  }

  getMin(): number {
    return this.values[0]
  }
}

const heap = new MinHeap()
heap.push(-2)
heap.push(0)
heap.push(-3)
if (heap.pop() !== -3) console.error('Wrong val')
if (heap.pop() !== -2) console.error('Wrong val')
if (heap.pop() !== 0) console.error('Wrong val')

console.log(-5, 0, -3, -4, 6, 2)
heap.push(-5, 0, -3, -4, 6, 2)
if (heap.pop() !== -5) console.error('Wrong val')
if (heap.pop() !== -4) console.error('Wrong val')
if (heap.pop() !== -3) console.error('Wrong val')
if (heap.pop() !== 0) console.error('Wrong val')
if (heap.pop() !== 2) console.error('Wrong val')
if (heap.pop() !== 6) console.error('Wrong val')

console.log(-2, 0, -1)
stack.push(-2, 0, -1)
if (stack.pop() !== -2) console.error('Wrong val')
if (stack.pop() !== -1) console.error('Wrong val')
if (stack.pop() !== 0) console.error('Wrong val')
