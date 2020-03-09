class MinStack {
    constructor() {
        this.values = [];
    }
    push(...x) {
        for (const val of x) {
            this._push(val);
        }
    }
    get last() {
        return this.values[this.values.length - 1];
    }
    _push(x) {
        if (this.values.length === 0) {
            this.values.push({ value: x, min: x });
        }
        else {
            const min = Math.min(x, this.last.min);
            this.values.push({ value: x, min });
        }
    }
    pop() {
        return this.values.pop().value;
    }
    top() {
        return this.last.value;
    }
    getMin() {
        return this.last.min;
    }
}
const stack = new MinStack();
stack.push(-2);
stack.push(0);
stack.push(-3);
if (stack.getMin() !== -3)
    console.error('Wrong val');
if (stack.pop() !== -3)
    console.error('Wrong val');
if (stack.getMin() !== -2)
    console.error('Wrong val');
if (stack.pop() !== 0)
    console.error('Wrong val');
if (stack.getMin() !== -2)
    console.error('Wrong val');
if (stack.pop() !== -2)
    console.error('Wrong val');
//# sourceMappingURL=minstack.js.map