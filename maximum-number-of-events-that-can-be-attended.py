from heapq import heappush, heappop
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap_elems = []
        max_day = max([ev[1] for ev in events])
        #heappush(heap_elems, [events[0][1], events[0][0]])
        current_day = events[0][0]
        curr_index = 0
        done_events = 0
        for i in range(current_day, max_day+1):
            both_finished = True
            if curr_index  < len(events):
                both_finished = False
                while i == events[curr_index][0]:
                    heappush(heap_elems, [events[curr_index][1], events[curr_index][0]])
                    curr_index += 1
                    if curr_index >= len(events):
                        break
            if len(heap_elems) > 0:
                ending_fast_event = heappop(heap_elems)
                while(ending_fast_event[0] < i):
                    if len(heap_elems) > 0:
                        ending_fast_event = heappop(heap_elems)
                    else:
                        ending_fast_event = None
                        break    
                if ending_fast_event and (not (ending_fast_event[0] < i)):
                    #print("Doing event ", ending_fast_event)
                    done_events += 1
                    both_finished = False
            if both_finished:
                return done_events
        return done_events
