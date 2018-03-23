# https://leetcode.com/problems/merge-k-sorted-lists/description/
# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.

import heapq
import random


class Solution(object):
  """
  :type lists: List[ListNode]
  :rtype: ListNode
  """

  def mergeKLists(self, lists):
    # [print_linked_list(l) for l in lists]
    heap = []
    refs = [None for x in lists]
    for k, kth_head in enumerate(lists):
      if kth_head:
        heapq.heappush(heap, (kth_head.val, k))
        refs[k] = kth_head.next

    head = None
    while len(heap):
      # get the smallest
      val, k = heapq.heappop(heap)
      new = ListNode(val)
      # print(k, refs)
      if refs[k]:
        # advance
        heapq.heappush(heap, (refs[k].val, k))
        refs[k] = refs[k].next
      if head is None:
        head = new
      else:
        node.next = new
      node = new
    # print_linked_list(head)
    return head

def list_to_linked_list(list):
  if list is None:
    return
  root = None
  for i, item in enumerate(list):
    next = ListNode(item)
    if i == 0:
      root = next
    else:
      node.next = next
    node = next
  return root

def print_linked_list(node):
  list = []
  while node is not None:
    list.append(node.val)
    node = node.next
  print(list)

def k_lists(k, max_len=6):
  return [list_to_linked_list(sorted([random.randint(0,9) for x in range(random.randint(1, max_len))])) for x in range(k)]

def lists_to_list_of_linked_lists(lists):
  return list(map(list_to_linked_list, lists))

# a = list(range(10))
# head = list_to_linked_list(a)
# print_linked_list(head)
# k = k_lists(4)
# [print_linked_list(l) for l in k]

# input = [
#   [1, 5, 9],
#   [2, 3, 6]
# ]

# class ListNode(object):
#   def __init__(self, x):
#     self.val = x
#     self.next = None

sol = Solution()
# sol.mergeKLists(lists_to_list_of_linked_lists(input))
# sol.mergeKLists(lists_to_list_of_linked_lists([None]))
sol.mergeKLists(lists_to_list_of_linked_lists([[],[1]]))


