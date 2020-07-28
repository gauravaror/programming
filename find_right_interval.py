import bisect
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        new_file = []
        new_file_idx = {}
        for idx,i in enumerate(intervals):
            new_file.append(i[0])
            new_file_idx[i[0]] = idx
        new_file.sort()
        output = []
        for i in intervals:
            im = bisect.bisect_left(new_file, i[1])
            #print(im, new_file)
            if im > len(new_file)-1:
                output.append(-1)
                continue
            num = new_file[im]
            idx = new_file_idx[num]
            if num >= i[1]:
                output.append(idx)
            else:
                output.append(-1)
        return output
