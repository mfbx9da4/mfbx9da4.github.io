# implement my queue which implements a queue via two stacks
# pg 111 and 240
# hints page 670: 98 114

class StackNode():
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next

class Stack():
  def __init__(self, val = None):
    self.top = StackNode(val)
    self.length = 0

  def push(self, val):
    new_top = StackNode(val, self.top)
    self.top = new_top
    self.length += 1

  def peek(self):
    return self.top

  def pop(self):
    val = self.top.val
    self.top = self.top.next
    self.length -= 1
    return val

class MyQueue():
  def __init__(self):
    self.stack = Stack()
    self.reverse_stack = Stack()

  def push(self, val):
    if self.reverse_stack.length > 0 and self.reverse_stack.length < self.stack.length:
      # some were removed
      # update self.stack
      self.pour_into_other(self.reverse_stack, self.stack)
    self.reverse_stack = Stack()
    self.stack.push(val)

  def pour_into_other(self, stack1, stack2):
    node = stack1.peek()
    while node.next != None:
      stack2.push(node.val)

  def update_reverse_stack(self):
    if self.reverse_stack.length:
      return 'Already up to date'
    self.pour_into_other(self.stack, self.reverse_stack)

  def pop(self):
    self.update_reverse_stack()
    self.reverse_stack.pop()


my_queue = MyQueue()
my_queue.push(1)
my_queue.push(2)
my_queue.push(3)

print my_queue.pop() == 1 and my_queue.pop() == 2 and my_queue.pop() == 3 and 'All tests passed'
