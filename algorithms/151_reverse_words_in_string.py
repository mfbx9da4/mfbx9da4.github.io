# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.strip().split()))
    
sol = Solution()
assert sol.reverseWords("the sky is blue") == "blue is sky the"
assert sol.reverseWords("  hello world!  ") == "world! hello"
assert sol.reverseWords("a good   example") == "example good a"
print('All tests passed ✅')