class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        map_guess =  Counter()
        map_secret = Counter()
        for s,g in zip(secret, guess):
            if s==g:
                bulls += 1
            else:
                map_guess[g] += 1
                map_secret[s] += 1
        for i,j in map_secret.items():
            if i in map_guess:
                cows += min(j, map_guess[i])
        return f'{bulls}A{cows}B'
                
        
