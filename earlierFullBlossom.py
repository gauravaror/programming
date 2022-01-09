class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        def possible(max_days):
            all_ = sorted(list(zip(plantTime, growTime)), key=lambda x: x[1], reverse= True)
            #print(all_)
            final_day = 0
            start_day = 0
            for i in all_:
                grow_finish = start_day + i[0]
                finish_day = grow_finish + i[1]
                final_day = max(final_day, finish_day)
                start_day = grow_finish
            return final_day <= max_days

        start = 0
        end = sum(plantTime) + max(growTime) + 1
        while start < end:
            mid = int((start + end) >> 1)
            #print(mid, possible(mid))
            if not possible(mid):
                start = mid + 1
            else:
                end = mid
        return start
       
        max_days = sum(plantTime) + max(growTime) + 1
        for i in range(1, max_days):
            print(i, possible(i))
        
