class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            x = 1<<i
            if x&n != 0:
                result = result|(1<<(31-i))
        return result