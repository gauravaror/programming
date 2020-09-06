class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        map_nums1 = defaultdict(list)
        map_nums2 = defaultdict(list)
        for idx,i in enumerate(nums1):
            map_nums1[i].append(idx)
        for idx,i in enumerate(nums2):
            map_nums2[i].append(idx)
        triplet1 = 0
        triplet2 = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]**2/nums2[j] in map_nums2:
                    poses = map_nums2[nums1[i]**2/nums2[j]]
                    indx = bisect.bisect_right(poses,j)
                    triplet1 += (len(poses) -indx)
                if nums2[j]**2/nums1[i] in map_nums1:
                    poses = map_nums1[nums2[j]**2/nums1[i]]
                    indx = bisect.bisect_right(poses,i)
                    triplet2 += (len(poses) - indx)
        print(nums1, nums2, triplet1, triplet2)
        return triplet1 + triplet2
