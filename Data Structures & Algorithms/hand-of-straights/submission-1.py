class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    
        if len(hand) % groupSize !=0:
            return False

        count = Counter(hand)

        for num in sorted(hand):
            if count[num]==0:
                continue
            
            for n in range(num, num+groupSize):
                if count[n] == 0:
                    return False
                count[n]-=1
            
        return True