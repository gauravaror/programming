class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        weights = {}
        for i in range(len(preferences)):
            for j in range(len(preferences[i])):
                weights[(i,preferences[i][j])] = j
        pairings = {}
        for i in pairs:
            pairings[i[0]] = i[1]
            pairings[i[1]] = i[0]

        def check_unhappy(a, b):
            if weights[(a,b)] == 0:
                return False
            baseline_weight = weights[(a,b)]
            for i in preferences[a]:
                if i == b:
                    return False
                if weights[(i,a)] < weights[(i, pairings[i])]:
                    return True
            return True
        output = 0
        #print(weights)
        for i in pairs:
            if check_unhappy(i[0], i[1]):
                output += 1
            #print(i[0], i[1], output)
            if check_unhappy(i[1], i[0]):
                output += 1
            #print(i[1], i[0], output)
        return output
                
