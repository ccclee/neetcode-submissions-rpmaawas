class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time +=1
        self.tweets[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        
        users = self.followMap[userId]
        users.add(userId)

        for uid in users:
            if self.tweets[uid]:
                index = len(self.tweets[uid])-1
                time, tweetId = self.tweets[uid][index]
                heapq.heappush(heap, (-time, tweetId, uid, index))

        while heap and len(res)<10:
            negTime, tweeId, uid, index = heapq.heappop(heap)
            res.append(tweeId)

            if index-1 >=0:
                prevTime, pretweetId = self.tweets[uid][index-1]
                heapq.heappush(heap, (-prevTime, pretweetId, uid, index-1))

        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.followMap[followerId].discard(followeeId)
        
