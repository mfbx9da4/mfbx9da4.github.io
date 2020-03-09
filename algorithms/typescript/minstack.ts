type Item = {
  value: number
  min: number
}

class MinStack {
  private values: Array<Item> = []

  push(...x: Array<number>) {
    for (const val of x) {
      this._push(val)
    }
  }

  private get last() {
    return this.values[this.values.length - 1]
  }

  private _push(x) {
    if (this.values.length === 0) {
      this.values.push({ value: x, min: x })
    } else {
      const min = Math.min(x, this.last.min)
      this.values.push({ value: x, min })
    }
  }

  pop(): number {
    return this.values.pop().value
  }

  top(): number {
    return this.last.value
  }

  getMin(): number {
    return this.last.min
  }
}

const stack = new MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
if (stack.getMin() !== -3) console.error('Wrong val')
if (stack.pop() !== -3) console.error('Wrong val')
if (stack.getMin() !== -2) console.error('Wrong val')
if (stack.pop() !== 0) console.error('Wrong val')
if (stack.getMin() !== -2) console.error('Wrong val')
if (stack.pop() !== -2) console.error('Wrong val')
