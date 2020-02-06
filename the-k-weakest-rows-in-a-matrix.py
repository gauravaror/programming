import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        num_rows = len(mat)
        num_people = len(mat[0])
        people = []
        for i in range(num_rows):
            soldiers = sum(mat[i])
            heapq.heappush(people, (soldiers, i))
        answer = []
        while len(answer) < k:
            temp = heapq.heappop(people)
            answer.append(temp[1])
        return answer
