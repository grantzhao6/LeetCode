class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import math
        while k > 0:
            gifts.sort()
            gifts.reverse()
            g = gifts[0]
            g = int(math.sqrt(g))
            gifts[0] = g
            k -= 1
        return sum(gifts)



        