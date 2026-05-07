class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] *=-1
        heapq.heapify(stones)
            
        while stones:
            if len(stones) <= 1:
                return -stones[0]
            else:
                biggest = - heapq.heappop(stones)
                second = - heapq.heappop(stones)
                if biggest > second:
                    newweight = - (biggest - second)
                    heapq.heappush(stones,newweight)


        return 0