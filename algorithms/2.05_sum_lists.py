x = [7, 1, 6]
y = [5, 9, 2]

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

def solve(head1, head2):
  node1 = head1
  node2 = head2
  remainder = 0
  prev = None
  while node1 is not None and node2 is not None:
    node1_val = node1.val if node1 else 0
    node2_val = node2.val if node2 else 0
    Sum = node1_val + node2_val + remainder

    res = Node(Sum % 10)
    remainder = Sum // 10

    if prev is None:
      res_head = res
    else:
      prev.next = res
    prev = res
    res = res.next

    node1 = node1.next
    node2 = node2.next
  return res_head


def solve_rec(head1, head2, carry=0):
  if head1 == None and head2 == None and carry == 0:
    return None

  total = carry
  if head1:
    total += head1.val

  if head2:
    total += head2.val

  digit = total % 10
  carry = 1 if total > 10 else 0
  ans = Node(digit)
  more = solve_rec(head1.next, head2.next, carry)
  ans.next = more
  return ans


head1 = list_to_linked_list(x)
head2 = list_to_linked_list(y)
print_list(head1)
print_list(head2)
print_list(solve(head1, head2))
print_list(solve_rec(head1, head2))
