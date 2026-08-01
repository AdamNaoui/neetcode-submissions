import heapq as hp
class Twitter:

    def __init__(self):
        self.tweets_by_user={}
        self.followers_by_user={}
        self.followees_by_user={}
        self.time=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets_by_user:
            self.tweets_by_user[userId]=[]
        
        hp.heappush(self.tweets_by_user[userId],(-self.time,userId,tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        followees=list(self.followees_by_user[userId]) if userId in self.followees_by_user else []

        feed_users=followees+[userId]

        res=[]
        reflow=[]

        for _ in range(10):
            newest=None
            for uId in feed_users:
                if uId not in self.tweets_by_user or not self.tweets_by_user[uId]:
                    continue

                if not newest or newest[0]>self.tweets_by_user[uId][0][0]:
                    newest=self.tweets_by_user[uId][0]
                
            if not newest:
                break
            print(newest)
            neg_time,uId,tweetId=newest
            hp.heappop(self.tweets_by_user[uId])
            res.append(tweetId)

            reflow.append(newest)
        
        #(-self.time,userId,tweetId))
        for neg_time,uId,tweetId in reflow:
            hp.heappush(self.tweets_by_user[uId],(neg_time,uId,tweetId))
            
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followees_by_user:
            self.followees_by_user[followerId]=set()

        self.followees_by_user[followerId].add(followeeId)
        
        if followeeId not in self.followers_by_user:
            self.followers_by_user[followeeId]=set()
        
        self.followers_by_user[followeeId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followees_by_user and followeeId in self.followees_by_user[followerId]:
            self.followees_by_user[followerId].remove(followeeId)
        
        if followeeId in self.followers_by_user and followerId in self.followers_by_user[followeeId]:
            self.followers_by_user[followeeId].remove(followerId)
