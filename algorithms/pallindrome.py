import pprint
pp = pprint.PrettyPrinter(indent=2)

class Solution(object):
  # each node will have values and children
  trie = {'values': None, 'children': {}}

  def palindromePairs(self, words):
    palindromes = []
    for i, word in enumerate(words):
      for j in range(i+1, len(words)):
        word2 = words[j]
        concat = word + word2
        if word == "" or word2 == "":
          palindromes += [[i, j], [j, i]]
          continue
        if self.isPallindrome(concat):
          palindromes.append([i, j])
        concat2 = word2 + word
        if self.isPallindrome(concat2):
          palindromes.append([j, i])
    return palindromes

  def isPallindrome(self, word):
    lo = 0
    hi = len(word) - 1
    while lo < hi:
      if word[lo] != word[hi]:
        return False
      lo += 1
      hi -= 1
    return True

  def addWordToTrie(self, word, id, reverse=False):
    palindromes = []
    prev = self.trie['children']
    if reverse:
      word = word[::-1]
    print word, id
    for j, char in enumerate(word):
      print j, char
      node = prev.get(char)
      if not node:
        node = {'values': [], 'children': {}}
        prev[char] = node
      is_last_letter = j == len(word) - 1

      if is_last_letter:
        # add children to palindromes
        children = self.get_children(node)
        node['values'].append(id)
        pp.pprint(self.trie)
        print('children', children)
        tuples = [[id, child] for child in children]
        palindromes += tuples
      prev = node['children']
    return palindromes

  def get_children(self, node):
    children = []
    open_list = [node]
    while len(open_list):
      node = open_list.pop()
      children += node['values']
      print('add these', children)
      open_list += [v for k, v in node['children'].items()]
    return children

  def palindromePairs2(self, words):
    palindromes = []
    for i, word in enumerate(words):
        palindromes += self.addWordToTrie(word, i)
        palindromes += self.addWordToTrie(word, i, reverse=True)
    return palindromes



# Examples
#
# Case1: If s1 is a blank string, then for any
# string that is palindrome s2, s1+s2 and s2+s1 are palindrome.
# e.g. s1 = "aba", s2 = ""
# "aba" + "" and "" + "aba" are pallindromes

# Case 2: If s2 is the reversing string of s1,
# then s1+s2 and s2+s1 are palindrome.
# e.g. s1 = "abc", s2 = "cba"
# "abc" + "cba" and "cba" + "abc" are pallindromes

# Case 3: If s1[0:cut] is palindrome and there
# exists s2 is the reversing string of s1[cut+1:] ,
# then s2+s1 is palindrome.
# e.g. s1 = "abacd", s2 = "dc", cut = 3 (denoted by `|`)
# "aba|cd" => "aba" is pallindrome, "dc" (s2) is reverse of "cd"
# => "dc" + "abacd" = s2 + s1 is pallindrome

# Case 4: Similiar to case3. If s1[cut+1: ] is
# palindrome and there exists s2 is the reversing
# string of s1[0:cut] , then s1+s2 is palindrome.
# e.g. s1 = "abcded", s2 = "cba", cut = 3 (denoted by `|`)
# "abc|ded" => "ded" is pallindrome, "cba" (s2) is reverse of "abc"
# => "abcded" + "cba" = s1 + s2 is pallindrome

_input = ["abcd", "dcba", "lls", "s", "sssll"]
expected =  [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["s", "sl", "llllllllls", "lllls"]
solver = Solution()
print solver.palindromePairs(_input)
