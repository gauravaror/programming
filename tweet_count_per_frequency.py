from collections import Counter
class TweetCounts:

    def __init__(self):
        self.hours = Counter()
        self.days = Counter()
        self.minutes = Counter()
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        minute = time//60
        hour = time//3600
        self.hours[tweetName+str(hour)] += 1
        self.minutes[tweetName+str(minute)] += 1
        self.days[tweetName+str(time)] += 1

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        start = startTime
        end =  endTime
        use_counter =  self.days
        if freq == 'hour':
            start = start //3600
            end = end//3600
            use_counter = self.hours
        elif freq == 'minute':
            start = start // 60
            end = end //60
            use_counter = self.minutes
        answer = []
        for i in range(start, end+1):
            key = tweetName + str(i)
            print(use_counter, i , key)
            if key in use_counter:
                answer.append(use_counter[key])
            #else:
                #answer.append(0)
        return answer
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
