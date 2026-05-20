class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        for i in range(32):
            x = 1<<i & n
            if x!= 0:
                bits +=1
        return bits
        