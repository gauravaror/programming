class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        def add_right(elem,idx):
            while len(deq) > 0 and  elem > deq[-1][0]:
                deq.pop()
            deq.append((elem,idx))
        
        def remove_left(elem, idx):
            while len(deq) > 0 and deq[0][1] <= idx:
                deq.popleft()
        
        for i in range(k):
            add_right(nums[i],i)

        output = [deq[0][0]]
        for j in range(k, len(nums)):
            remove_left(nums[j-k], j-k)
            add_right(nums[j], j)
            output.append(deq[0][0])
        return output
