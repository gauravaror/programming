class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        ind1 = 0
        ind2 = 0
        ind3 = 0
        output = []
        while ind1<len(arr1) and ind2 < len(arr2) and ind3 < len(arr3):
            print(ind1, ind2, ind3)
            elem1 = arr1[ind1]
            elem2 = arr2[ind2]
            elem3 = arr3[ind3]
            if elem1 == elem2 == elem3:
                output.append(elem1)
                ind1 += 1
                ind2 += 1
                ind3 += 1
            elif arr1[ind1] < arr2[ind2]:
                ind1 += 1
            elif arr2[ind2] < arr1[ind1]:
                ind2 += 1
            elif arr1[ind1] < arr3[ind3]:
                ind1 += 1
            elif arr3[ind3] < arr1[ind1]:
                ind3 += 1
            elif arr2[ind2] < arr3[ind3]:
                ind2 += 1
            elif arr3[ind3] < arr2[ind2]:
                ind3 += 1
        return output
