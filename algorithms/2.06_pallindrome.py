class Node():
  def __init__(self, val = None, next = None):
    self.val = val
    self.next = next

def list_to_linked_list(arr):
  prev = None
  for val in arr:
    node = Node(val)
    if prev:
      prev.next = node
    else:
      head = node
    prev = node
  return head

def print_list(node):
  l = list()
  while node != None:
    l.append(node.val)
    node = node.next
  print l

def solve(node):
  stack = []

  slow = node
  fast = node
  while fast != None and fast.next != None:
    stack.append(slow.val)
    slow = slow.next
    fast = fast.next.next

  if fast != None:
    slow = slow.next

  while len(stack):
    val = stack.pop()
    if val != slow.val:
      return False
    slow = slow.next
  return True



x = ['a', 'b', 'a']
x = ['a', 'b', 'b', 'a']
x = ['a', 'b', 'c', 'e', 'f', 'd', 'c', 'b', 'a']
x = ['a', 'b', 'c', 'd', 'f', 'd', 'c', 'b', 'a']
head1 = list_to_linked_list(x)
print_list(head1)
print(solve(head1))
