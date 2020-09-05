class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        seq_left = []
        seq_right = []
        seq_left.append(0)
        seq_right.append(len(arr)-1)
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                break
            else:
                seq_left.append(i)
        for i in range(len(arr)-2,-1,-1):
            if arr[i+1] < arr[i]:
                break
            else:
                seq_right.append(i)
        print(seq_left, seq_right)
        min_length = len(arr) - max(len(seq_left), len(seq_right))
        for i in seq_left[::-1]:
            if i == seq_right[-1]:
                return 0
            if arr[seq_right[-1]] >= arr[i]:
                min_length = min(min_length, seq_right[-1] - i -1)
        for j in seq_right[::-1]:
            if arr[seq_left[-1]] <= arr[j]:
                min_length = min(min_length, j-seq_left[-1]-1)
        return min_length

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        seq_left = []
        seq_right = []
        seq_left.append(0)
        seq_right.append(len(arr)-1)
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                break
            else:
                seq_left.append(i)
        for i in range(len(arr)-2,-1,-1):
            if arr[i+1] < arr[i]:
                break
            else:
                seq_right.append(i)
        print(seq_left, seq_right)
        min_length = len(arr) - max(len(seq_left), len(seq_right))
        for i in seq_left:
            for j in seq_right:
                if i == j:
                    return 0
                if arr[i] <= arr[j]:
                    min_length = min(min_length, j-i-1)
        return min_length
                    
