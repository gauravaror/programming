class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for i in asteroids:
            if i > 0:
                stack.append(i)
            else:
                finished = False
                while stack:
                    if not (stack[-1] > 0 and i < 0):
                        break
                    if abs(stack[-1]) > abs(i):
                        finished = True
                        break
                    elif abs(stack[-1]) == abs(i):
                        finished = True
                        stack.pop()
                        break
                    else:
                        stack.pop()
                if not finished:
                    stack.append(i)
        return list(stack)
                        
                
