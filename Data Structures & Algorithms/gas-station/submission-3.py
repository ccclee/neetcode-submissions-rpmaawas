class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        station = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            tank += diff
            total += diff
            if tank<0:
                tank = 0
                station = i+1
        
        return -1 if total<0 else station
        