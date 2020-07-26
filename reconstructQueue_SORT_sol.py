class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda h: (-h[0],h[1]))
        print(people)
        queue = []
        for p in people:
            #print(queue)
            queue.insert(p[1], p)
        return queue
