class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        maximum_days = max([e[1] for e in events])
        len_days = len(events)
        days = {}
        total_events = []
        total_days = []
        for idx, event in enumerate(events):
            total_events.append(idx)
            for i  in range(event[0], event[1]+1):
                total_days.append(i)
                if i in days:
                    days[i].append(idx)
                else:
                    days[i] = [idx]
        total_days = list(set(total_days))
        def backtrack(day, left_events):
            max_events = 0
            any_event = False
            if len(left_events) == 0:
                return 0
            if day < len(total_days):
                for aev in days[total_days[day]]:
                    if aev in left_events:
                        left_events.remove(aev)
                        ans = backtrack(day+1, left_events)
                        if max_events < ans + 1:
                            max_events = ans + 1
                        left_events.append(aev)
                    else:
                        ans = backtrack(day+1, left_events)
                        if max_events < ans:
                            max_events = ans 
            return max_events
        return backtrack(0, total_events)
