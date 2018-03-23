class Node:
  def __init__(self, **entries):
    self.__dict__.update(entries)

class MinHeap(object):
  """docstring for MinHeap"""
  def __init__(self, root):
    self.root = Node(**{'l': None, 'r': None, 'parent': None, 'val': root})
    self.rightmost = self.root
    self.size = 1

  def push(self, val):
    node = Node(**{'val': val, 'l': None, 'r': None, 'parent': self.rightmost})
    if self.rightmost.r:
      self.rightmost.l = node
    else:
      self.rightmost.r = node
    self.siftup(val, node)
    self.size += 1

  def siftup(self, val, node):
    while node.parent and node.parent.val > val:
      parent_val = node.parent.val
      node.parent.val = val
      node.val = parent_val
      node = node.parent
    self.update_rightmost()
    return node

  def update_rightmost(self):
    stack = [self.root]
    while 1:
      node = stack.pop(0)
      if node.l is None or node.r is None:
        self.rightmost = node
        break
      stack.append(node.l)
      stack.append(node.r)

  def pop(self):
    # remove min
    # swap rightmost with root
    # percolate down
    # update rightmost
    min_val = self.root.val
    if self.rightmost.l:
      print('left', self.rightmost.l.val)
      self.root.val = self.rightmost.l.val
      self.rightmost.l = None
    elif self.rightmost.r:
      print('right', self.rightmost.r.val)
      self.root.val = self.rightmost.r.val
      self.rightmost.r = None
    else:
      print('full', self.rightmost.val)
      self.root.val = self.rightmost.val
      if self.rightmost.parent.l == self.rightmost:
        self.rightmost.parent.l = None
      if self.rightmost.parent.r == self.rightmost:
        self.rightmost.parent.r = None
      self.rightmost = None

    node = self.root
    while 1:
      val = node.val
      # swap with min of left and right
      left_val = node.l.val if node.l else None
      right_val = node.r.val if node.r else None
      if (left_val and val > left_val) or (right_val and val > right_val):
        # if greater than either left or right
        if left_val is None:
          node.val = node.r.val
          node.r.val = val
          node = node.r
        elif right_val is None:
          node.val = node.l.val
          node.l.val = val
          node = node.l
        elif left_val < right_val:
          print('left', node.l.val)
          node.val = node.l.val
          node.l.val = val
          node = node.l
        else:
          print('right', node.r.val)
          node.val = node.r.val
          node.r.val = val
          node = node.r
      else:
        break

    self.update_rightmost()

    return min_val


  def __str__(self):
    queue = [(self.root, 0)]
    out = ''
    while len(queue):
      node, level = queue.pop(0)
      if node:
        out += '  ' * (level) +  str(node.val).zfill(2)
        if node.l:
          out += ' l:' + str(node.l.val).zfill(2)
          queue.append((node.l, level + 1))
        if node.r:
          out += ' r:' + str(node.r.val).zfill(2)
          queue.append((node.r, level + 1))
        out += '\n'
    return out


minheap = MinHeap(7)
minheap.push(8)
minheap.push(12)
minheap.push(15)
minheap.push(13)
minheap.push(2)
minheap.push(10)
print(minheap)
print('popped', minheap.pop())
print(minheap)
print('popped', minheap.pop())
print(minheap)
print('popped', minheap.pop())
print(minheap)
print('popped', minheap.pop())
print(minheap)
