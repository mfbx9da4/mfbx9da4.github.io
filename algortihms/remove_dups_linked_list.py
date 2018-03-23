class Node():
  """docstring for Node"""
  def __init__(self, val):
    self.val = val
    self.next = None

linked = []
prev = None
for x in xrange(1,10):
  node = Node(x % 3)
  if not prev:
    head = node
  else:
    prev.next = node
  prev = node

def solve(node):
  seen = set()
  while node != None:
    if node.val in seen:
      print('val', node.val)
      prev.next = node.next
    else:
      seen.add(node.val)
      prev = node
    node = node.next

def print_list(node):
  l = list()
  while node != None:
    l.append(node.val)
    node = node.next
  print l

print_list(head)
print(solve(head))
print_list(head)
