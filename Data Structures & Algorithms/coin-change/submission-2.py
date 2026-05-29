class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse =True)
        mincoin = {}
        mincoin[0]=0
        for coin in coins:
            mincoin[coin]=1
        
        def findmin(left):
            if left in mincoin:
                return mincoin[left]
            
            else:
                curr =10001
                for coin in coins:
                    if coin<=left:
                        curr = min(curr, 1+ findmin(left-coin))
                mincoin[left] = curr
                return curr
        
        res = findmin(amount)

        return -1 if res>10000 else res

