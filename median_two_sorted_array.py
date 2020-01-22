from typing import List
import math

def get_index(number: int, nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    cl = math.ceil(len(nums) / 2)
    if nums[cl] > number:
        return cl - (cl - get_index(number, nums[:cl]))
    else:
        return cl + get_index(number, nums[cl:])
    
def merge(nums1: List[int], nums2: List[int], index: int, even: bool) -> float:
    if len(nums1) == 0:
        if even:
            return (nums2[index] + nums2[index+1])/2
        else:
            return nums2[index]
    list_tap_index = get_index(nums1[0], nums2)
    new_index = index - (list_tap_index + 1)
    print("Merging ", nums1, nums2, list_tap_index, new_index, index, even)
    if new_index >= 0:
        move_index = 1
        if new_index == 0:
            move_index = 0
        if list_tap_index + 1 >= len(nums2):
            return merge([], nums1[move_index:], new_index-move_index, even)
        if move_index >= len(nums1):
            return merge([], nums2[(list_tap_index+1):], new_index-move_index, even)
        if nums2[list_tap_index + 1] > nums1[move_index]:
            return merge(nums2[(list_tap_index+1):], nums1[move_index:], new_index-move_index, even)
        else:
            return merge(nums1[move_index:], nums2[(list_tap_index+1):], new_index-move_index, even)
    else:
        if even:
            if (index + 1) <= list_tap_index:
                return (nums2[index] + nums2[index + 1])/ 2
            elif index <= list_tap_index:
                return (nums2[index] + nums1[0])/2
        else:
            if index <= list_tap_index:
                return nums2[index]
            else:
                return nums1[0]

def get_median(nums1: List[int]) -> float:
    index = math.ceil(len(nums1)/2) - 1
    if len(nums1) % 2 == 0:
        return (nums1[index] + nums1[index+1])/2
    else:
        return nums1[index]


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    n = len(nums1) + len(nums2)
    if len(nums1) == 0:
        return get_median(nums2)
    elif len(nums2) == 0:
        return get_median(nums1)
    elif nums1[0] > nums2[0]:
        return merge(nums1, nums2, math.ceil(n/2) - 1, (n %  2 == 0))
    else:
        return merge(nums2, nums1, math.ceil(n/2) - 1, (n % 2 == 0))

print(findMedianSortedArrays([1,2], [-1,3]))
assert findMedianSortedArrays([1,2], [-1,3]) == 1.5
assert findMedianSortedArrays([2,2,2], [2,2,2,2]) == 2
assert findMedianSortedArrays([2,2,2,2], [2,2,2]) == 2
assert findMedianSortedArrays([1,2,4,5,6], [3,7,9,10]) == 5
assert findMedianSortedArrays([1,2], [3,4]) == 2.5
assert findMedianSortedArrays([], [1]) == 1
assert findMedianSortedArrays([1], [2,3]) == 2
assert findMedianSortedArrays([2], [1,3,4,5]) == 3
