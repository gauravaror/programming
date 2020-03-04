from collections import Counter
from functools import cmp_to_key
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        total_pos = len(votes[0])
        unique_teams = []
        counter_votes = [Counter() for _ in range(total_pos)]
        for idx,i in enumerate(votes):
            for j in range(len(i)):
                if not i[j] in unique_teams:
                    unique_teams.append(i[j])
                counter_votes[j][i[j]] += 1
        total_sceme = []
        for i in unique_teams:
            this_votes = []
            for j in range(total_pos):
                curr_pref = 0
                if i in counter_votes[j]:
                    curr_pref = counter_votes[j][i]
                this_votes.append(curr_pref)
            this_votes.append(i)
            total_sceme.append(tuple(this_votes))
        #print(total_sceme)
        def our_comp(A, B):
            dlen = len(A)
            for i in range(dlen):
                if i == (dlen-1):
                    if A[i] < B[i]:
                        return 1
                    else:
                        return -1
                if not (A[i] == B[i]):
                    if A[i] < B[i]:
                        return -1
                    else:
                        return 1
                
        total_sceme = sorted(total_sceme, key=cmp_to_key(our_comp))
        #print(total_sceme)
        output = ""
        for i in total_sceme[::-1]:
            last = len(i)
            output += i[last-1]
        return output
