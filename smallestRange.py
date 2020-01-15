from typing import List
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        ranges = {}
        nums = sorted(nums, key=lambda x: x[0])
        def get_current_range():
            first = nums[0][0]
            last = nums[-1][0]
            if (last-first) not in ranges:
                ranges[last-first] = [first, last]

        def move_next():
            changing_index = 0
            while len(nums[changing_index]) == 1:
                changing_index += 1
                if (changing_index >= len(nums)):
                    return -1
            return changing_index

        def find_position(element):
            if len(nums) == 0:
                return 0
            start = 0
            end  = len(nums)
            mid = (start + end) // 2
            while (start < end):
                mid  = (start + end) // 2
                #print(start, end, mid)
                if (nums[mid][0] > element):
                    end = mid - 1
                else:
                    start = mid + 1
            mid = (start + end) // 2
            if mid < 0:
                return 0
            return mid

        index = 0
        while True:
            get_current_range()
            index  = move_next()
            if (index == -1 or index >= len(nums)):
                break
            append_list = nums[index][1:]
            nums.pop(index)
            elem = find_position(append_list[0])
            if elem < len(nums):
                if (nums[elem][0] < append_list[0]):
                    elem = elem + 1

            nums.insert(elem, append_list)
            #print(index, nums, elem)
            #nums[index] = nums[index][1:]
            #nums = sorted(nums, key=lambda x: x[0])
        #print(ranges)
        min_elem = min(ranges.items(), key=lambda x:x[0])
        return min_elem[1]

sol = Solution()
print(sol.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))
