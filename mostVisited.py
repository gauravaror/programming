class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        if rounds[-1] < rounds[0]:
            la = list(range(rounds[0], n+1))
            lb = list(range(1, rounds[-1]+1))
            return  lb + la 
        else:
            return range(rounds[0], rounds[-1]+1)
