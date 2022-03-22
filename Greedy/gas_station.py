# https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if (sum(gas) - sum(cost) < 0): # 🔑
            return -1
        
        start_index = 0
        tank = 0
        for i, value in enumerate(gas):
            print(f'tank: {tank}, gas: {gas[i]}, cost: {cost[i]}')
            tank += gas[i] - cost[i]
            print(f'tank: {tank}')
            if tank < 0:
                start_index = i + 1
                tank = 0
        return start_index
