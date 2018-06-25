def validate(nodes, i, lo, hi):
  cur = nodes[i]
  print('nodes, i, lo, hi', nodes, i, cur, lo, hi)

  if i == len(nodes) - 1:
    return i

  next = nodes[i + 1]
  valid_left = None
  valid_right = None

  # left
  if next < cur:
    if lo is None or next > lo:
      valid_left = validate(nodes, i + 1, lo, cur)

  # right
  if valid_left is not None:
    k = valid_left + 1
  else:
    k = i + 1
  next = nodes[k]
  if next > cur:
    if hi is None or next < hi:
      valid_right = validate(nodes, k, cur, hi)

  return valid_right or valid_left or i

def solve(nodes):
  i = validate(nodes, 0, None, None)
  if i == len(nodes) - 1:
    return 'valid'
  return 'not valid'


array = [3, 2, 1, 5, 4, 6]
assert solve(array) == 'valid'
array = [3, 5, 2]
assert solve(array) == 'not valid'
array = [3, 5, 6, 7, 8]
assert solve(array) == 'valid'
array = [3, 5, 6, 7, 8, 2]
assert solve(array) == 'not valid'
