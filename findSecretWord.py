# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

import random
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        done_guesses = 0
        while len(wordlist)  > 0:
            g = random.randint(0, len(wordlist)-1)
            #g = 0
            print(done_guesses, g, wordlist[g])
            done_guesses += 1
            matches = master.guess(wordlist[g])
            if matches == 6:
                break
            newList = []
            for i in wordlist:
                #print(i, wordlist[g])
               # if i == wordlist[g]:
                #    continue
                score = 0
                for t,k in zip(wordlist[g], i):
                    if t == k:
                        score += 1
                print(i, score, matches)
                if score == matches:
                    newList.append(i)
            wordlist = newList
            print(wordlist)
