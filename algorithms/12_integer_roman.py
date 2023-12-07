# https://leetcode.com/problems/integer-to-roman/

roman = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
]

class Solution:
    def intToRoman(self, num: int) -> str:
        remaining = num
        chars = ''
        while remaining > 0:
            for (val, char) in roman:
                if val <= remaining:
                    chars += char
                    remaining -= val
                    break
        return chars
    
sol = Solution()
assert sol.intToRoman(20) == 'XX'
assert sol.intToRoman(3) == 'III'
assert sol.intToRoman(4) == 'IV'
assert sol.intToRoman(9) == 'IX'
assert sol.intToRoman(58) == 'LVIII'
print('All tests passed ✅')