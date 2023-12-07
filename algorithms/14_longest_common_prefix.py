# https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        assert len(strs) >= 1
        shortest = min(strs, key=lambda x: len(x))
        hi = len(shortest) + 1
        lo = 0
        best = ''

        def all_have_prefix(prefix):
            for s in strs:
                if not s.startswith(prefix):
                    return False
            return True
        
        while True:
            mid = lo + ((hi - lo) // 2)
            prefix = shortest[0:mid]
            if lo > hi:
                break
            if all_have_prefix(prefix):
                best = prefix
                lo = mid + 1
            else:
                hi = mid - 1
        return best


sol = Solution()
assert sol.longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert sol.longestCommonPrefix(["dog","racecar","car"]) == ""
assert sol.longestCommonPrefix(["a"]) == "a"
assert sol.longestCommonPrefix(["cir","car"]) == "c"

print('All tests passed ✅')