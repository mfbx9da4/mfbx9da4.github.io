# https://leetcode.com/problems/roman-to-integer

d = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

p = {
    'I': ['V', 'X'],
    'X': ['L', 'C'],
    'C': ['D', 'M'],
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            x = s[i]
            if x in p and i < len(s) - 1 and s[i + 1] in p[x]:
                total += d[s[i + 1]] - d[x]
                i += 2
            else:
                total += d[x]
                i += 1
        return total
        

sol = Solution()
assert sol.romanToInt("III") == 3
assert sol.romanToInt("IV") == 4
assert sol.romanToInt("IX") == 9
assert sol.romanToInt("LVIII") == 58
assert sol.romanToInt("MCMXCIV") == 1994

print('All tests passed ✅')