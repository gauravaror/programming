from collections import deque
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free_servers = []
        for idx,weight in enumerate(servers):
            heappush(free_servers, (weight, idx))
        second = 0
        current_task = []
        output = [-1]*len(tasks)
        available_tasks = deque()
        while second < len(tasks) or len(available_tasks) > 0:
            while len(current_task) > 0 and current_task[0][0] <= second:
                s, idx = heappop(current_task)
                heappush(free_servers, (servers[idx], idx))
            if second < len(tasks):
                available_tasks.append(second)
            while len(free_servers) > 0 and len(available_tasks) > 0:
                this_task = available_tasks.popleft()
                task_seconds = tasks[this_task]
                w,idx = heappop(free_servers)
                output[this_task] = idx
                heappush(current_task, (second + task_seconds, idx))
            move = 1
            if second >= len(tasks) and len(free_servers) == 0 and len(current_task) > 0 and current_task[0][0] > second + 1:
                move = current_task[0][0]
                second = move
            else:
                second += 1
        return output
