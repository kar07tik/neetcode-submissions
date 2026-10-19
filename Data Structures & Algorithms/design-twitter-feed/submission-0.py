from collections import defaultdict

class Twitter:
    def __init__(self):
        self.tweets=defaultdict(list)
        self.following=defaultdict(set)
        self.time=0

    def postTweet(self,userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self,userId: int) -> list[int]:
        users = self.following[userId] | {userId}
        feed=[]

        for user in users:
            feed.extend(self.tweets[user])

        feed.sort(reverse=True)
        return [tweetId for _, tweetId in feed[:10]]
    def follow(self,followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self,followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        