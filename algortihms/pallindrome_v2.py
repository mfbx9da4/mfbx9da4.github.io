# original problem
# https://leetcode.com/problems/palindrome-pairs/description/
# Given a list of unique words, find all pairs of distinct
# indices (i, j) in the given list, so that the concatenation
# of the two words, i.e. words[i] + words[j] is a palindrome.



import pprint
pp = pprint.PrettyPrinter(indent=2)

class Solution(object):
  def palindromePairs(self, words):
    # where we will store output
    out = []

    # a hash map of each word to it's index
    # words are unique!
    word_to_index = { word: i for i, word in enumerate(words) }

    # used for caching, avoid recalculating if
    # a word is a pallindrome if we have already done that
    self.is_pallindrome_cache = {}

    blank_id = word_to_index.get("")
    for i, word in enumerate(words):

      # Case1: "aba" + "" and "" + "aba" are pallindromes
      if len(word) > 0 and blank_id is not None and self.is_pallindrome(word):
        out += [[i, blank_id], [blank_id, i]]

      # Case 2: "abc" + "cba" and "cba" + "abc" are pallindromes
      reverse = word[::-1]
      reverse_i = word_to_index.get(reverse)
      if reverse_i is not None and i != reverse_i:
        out.append([i, reverse_i])

      for cut in range(1, len(word)):
        cut_l = word[:cut]
        cut_r = word[cut:]
        cut_l_reverse = cut_l[::-1]
        cut_l_reverse_id = word_to_index.get(cut_l_reverse)
        cut_r_reverse = cut_r[::-1]
        cut_r_reverse_id = word_to_index.get(cut_r_reverse)

        # Case 3: If s1[cut:] (cut_r) is palindrome and
        # there exists s2 which is the reverse of
        # s1[0:cut], then s1+s2 is palindrome.
        # e.g. s1 = "abcded", s2 = "cba", cut = 3 (denoted by `|`)
        # "abc|ded" => "ded" is pallindrome, "cba" (s2) is reverse of "abc"
        # => "abcded" + "cba" = s1 + s2 is pallindrome
        if cut_l_reverse_id is not None and self.is_pallindrome(cut_r):
          out.append([i, cut_l_reverse_id])

        # Case 4: If s1[0:cut] (cut_l) is palindrome and there
        # exists s2 which is the reverse of s1[cut:],
        # then s2+s1 is palindrome.
        # e.g. s1 = "abacd", s2 = "dc", cut = 3 (denoted by `|`)
        # "aba|cd" => "aba" is pallindrome, "dc" (s2) is reverse of "cd"
        # => "dc" + "abacd" = s2 + s1 is pallindrome
        if cut_r_reverse_id is not None and self.is_pallindrome(cut_l):
          out.append([cut_r_reverse_id, i])

    return out

  def is_pallindrome(self, word):
    is_palli = self.is_pallindrome_cache.get(word)
    if is_palli is not None:
      return is_palli
    lo = 0
    hi = len(word) - 1
    is_palli =  True
    while lo < hi:
      if word[lo] != word[hi]:
        is_palli =  False
        break
      lo += 1
      hi -= 1
    self.is_pallindrome_cache[word] = is_palli
    return is_palli


_input = ["abcd", "dcba", "lls", "s", "sssll"]
_input = ["a","abc","aba",""]
expected =  [[0, 1], [1, 0], [3, 2], [2, 4]]
print(_input)
# The palindromes are ["s", "sl", "llllllllls", "lllls"]
solver = Solution()
print solver.palindromePairs(_input)
