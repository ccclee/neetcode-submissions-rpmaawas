class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = n
        count = 0
        while temp>=1:
            if temp%2 != 0:
                count+=1
            temp = temp//2
        return count
        