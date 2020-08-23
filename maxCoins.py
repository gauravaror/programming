class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        even = False
        mycoins = 0
        total_times = len(piles)//3
        newpile = piles[total_times:]
        print(newpile)
        for i in range(0, len(newpile),2):
            mycoins += newpile[i]
        return mycoins
