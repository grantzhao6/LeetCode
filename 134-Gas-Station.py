class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        scost = sum(cost)
        sgas = sum(gas)

        if scost > sgas:
            return -1

        total = 0
        index = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                index = i + 1

        return index
        