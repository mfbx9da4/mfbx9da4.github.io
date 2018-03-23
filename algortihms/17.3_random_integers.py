# generate a set of m integers from an array of size n
# without random lib
#
# random number, split over length
# choose one, reduce size,
# all numbers greater should now be -1 index
# [ 0 1 2 3 4 X 6 7 8 ] original numbers
# [           + + + 8 ]
# [ 0 1 2 3 4 6 7 8 | ]
#
# assume m < n:
#
# while len(m) < m :
#   build it up
#   k = floor(rand * remaining)
#   subset.append(n[k])
#
# ensure unique / shuffle
#
# or include all and remove some
#
# or binary search into halves until size
# is equal
#

# how is randint implemented?
# how is sample implemented?
# how is randomness implemented?

import random
import math

def random_subset(orig, len_subset):
  subset = []
  for i in range(len_subset):
    subset.append(orig[i])

  for i, x in enumerate(orig):
    r_index = math.floor(random.random() * (i + 2))
    if r_index < len_subset:
      print('swap', subset[r_index], 'at', r_index, 'for', x)
      subset[r_index] = x
    else:
      print('dont swap', x)
  print(subset)


def sample(array):
  """Unique random subset generator"""
  copy = [x for x in array]
  while len(copy) > 0:
    ri = random.randint(0, len(copy) - 1)
    print(ri, len(copy))
    yield copy.pop(ri)

random_set = list(range(10))
m = 5
# random_subset(random_set, m)
out = [x for x in sample(random_set)]
print(out)
assert out != random_set
assert sorted(out) == random_set
