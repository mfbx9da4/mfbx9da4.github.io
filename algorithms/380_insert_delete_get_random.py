# https://leetcode.com/problems/insert-delete-getrandom-o1/
import random

class RandomizedSet:
    def __init__(self):
      self._dict = dict()
      self._array = list()

    def insert(self, val: int) -> bool:
      if val in self._dict: return False
      self._dict[val] = len(self._array)
      self._array.append(val)
      return True

    def remove(self, val: int) -> bool:
      if val not in self._dict: return False
      i = self._dict[val]
      # Swap the last element with the element to delete
      self._array[i], self._array[-1] = self._array[-1], self._array[i]
      # Update the index of the swapped element
      self._dict[self._array[i]] = i 
      # Delete the last element
      self._array.pop()
      # Delete the element from the dict
      del self._dict[val]
      return True

    def getRandom(self) -> int:
      i = random.randint(0, len(self._array) - 1)
      return self._array[i]


# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]
def test(ops, args, expected):
  obj = RandomizedSet()
  for op, arg, exp in zip(ops, args, expected):
    print(obj._array)
    print(f'{op}({arg[0] if len(arg) > 0 else ""}) -> {exp}')
    if op == 'insert':
      assert obj.insert(arg[0]) == exp
    elif op == 'remove':
      assert obj.remove(arg[0]) == exp
    elif op == 'getRandom':
      assert obj.getRandom() == exp
    elif op == 'RandomizedSet':
      pass
    else:
      raise ValueError(f'Invalid operation {op}')

ops = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
args = [[], [1], [2], [2], [], [1], [2], []]
expected = [None, True, False, True, 2, True, False, 2]
test(ops, args, expected)

print('All tests passed ✅')