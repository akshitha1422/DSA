class Twitter:

    def __init__(self):
        self.time=0
        self.tweets=[]
        self.following={}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweets.append((self.time,userId,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        followees=self.following.get(userId,set())
        followees=followees.union({userId})
        for t,uid,tid in reversed(self.tweets):
            if uid in followees:
                res.append(tid)
                if len(res)==10:
                    break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId]=set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)