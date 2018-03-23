x = [3, 2, 4, 5, 8, 5, 10, 2, 1]
# x = [10, 2]

def list_to_linked_list(arr):
  prev = None
  for val in arr:
    node = {}
    node['val'] = val
    node['next'] = None
    if prev:
      prev['next'] = node
    else:
      head = node
    prev = node
  return head

def print_list(node):
  l = list()
  while node != None:
    l.append(node['val'])
    node = node['next']
  print l

def solve(partition_x, node):
  """
  could be simplified with separate linked list
  """
  prev = None
  head = node
  while node is not None:
    next_node = node['next']

    if prev is not None and node['val'] < partition_x:
      # if we are not at head and
      # if cur is less than x
      # move cur to beginning
      node['next'] = head
      head = node
      # and point prev to next node
      prev['next'] = next_node
    else:
      # we did not move the current node
      # so it is now the prev
      prev = node

    node = next_node
  return head

head = list_to_linked_list(x)
print_list(head)
print_list(solve(5, head))

