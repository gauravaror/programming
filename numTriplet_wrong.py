class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        map_nums1 = defaultdict(list)
        map_nums2 = defaultdict(list)
        for idx,i in enumerate(nums1):
            map_nums1[i].append(idx)
        for idx,i in enumerate(nums2):
            map_nums2[i].append(idx)
        
            
        triplet = 0
        for n1,pos1 in map_nums1.items():
            for n2,pos2 in map_nums2.items():
                if n1**2/n2 in map_nums2:
                    otherpos1 = map_nums2[n1**2/n2]
                    for checkpos in otherpos1:
                        for cpos in pos2:
                            if checkpos != cpos:
                                triplet += 1
                if n2**2/n1 in map_nums1:
                    otherpos2 = map_nums1[n2**2/n1]
                    for checkpos in otherpos2:
                        for cpos in pos1:
                            if checkpos != cpos:
                                triplet += 1
        return triplet
    
                    
        
