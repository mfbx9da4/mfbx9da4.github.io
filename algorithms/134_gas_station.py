# https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        if sum(gas) < sum(cost): return -1
        total = 0
        start = 0
        for i in range(len(gas)):
            if total < 0:
                print(f'total = {total} < 0')
                total = 0
                start = i
            total += gas[i] - cost[i]

        return start
    

sol = Solution()
# assert sol.canCompleteCircuit(
#     [1,2,3,4,5], 
#     [3,4,5,1,2]) == 3

# assert sol.canCompleteCircuit(
#     [2,3,4],
#     [3,4,3]) == -1

assert sol.canCompleteCircuit(
    [5,1,2,3,4],
    [4,4,1,5,1]) == 4
print('All tests passed ✅')