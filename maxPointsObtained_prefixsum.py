class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cumsum = 0
        sum1 = [0]
        sum2 = [0]
        for i in range(len(cardPoints)):
            cumsum += cardPoints[i]
            sum1.append(cumsum)
        cumsum = 0
        for i in range(len(cardPoints)-1, -1, -1):
            cumsum += cardPoints[i]
            sum2.append(cumsum)
        #print(sum1, sum2)
        maxa = 0
        for i in range(k+1):
            maxa = max(maxa, sum1[i] + sum2[k-i])
        return maxa
