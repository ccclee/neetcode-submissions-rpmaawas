class MedianFinder:

    def __init__(self):
        self.nums =[]
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()
        

    def findMedian(self) -> float:
        length = len(self.nums)
        if length%2 ==0:
            return (self.nums[int(length/2)] + self.nums[int(length/2)-1])/2
        return self.nums[int((length-1)/2)]

        
        