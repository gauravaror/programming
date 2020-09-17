class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 00 01 02
        # 10 11 12
        # 20 21 22
        # 01 -> 10 -> 0-1 -> -10 -> 01
        # 01 -> 0-1 -> -10 -> 10 -> 01
        R = {(0,1): (1,0), (1,0):(0,-1), (0,-1): (-1,0), (-1,0): (0,1)}
        L = {(0,1): (-1,0), (-1,0): (0,-1), (0,-1): (1,0), (1,0): (0,1)}
        initial_dir = (0,1)
        initial_state = (0,0)
        prev_states = set()
        prev_states.add((initial_state,initial_dir))
        print(instructions)
        def perform_instruction():
            nonlocal initial_state, initial_dir
            for i in instructions:
                #print(i, initial_state, initial_dir)
                if i == 'L':
                    initial_dir = L[initial_dir]
                elif i == 'R':
                    initial_dir = R[initial_dir]
                else:
                    initial_state = (initial_state[0] + initial_dir[0],
                                    initial_state[1] + initial_dir[1])
        perform_instruction()
        first = abs(initial_state[0]) + abs(initial_state[1])
        perform_instruction()
        second = abs(initial_state[0]) + abs(initial_state[1])
        perform_instruction()
        third = abs(initial_state[0]) + abs(initial_state[1])
        perform_instruction()
        fourth = abs(initial_state[0]) + abs(initial_state[1])
        print(first, second, third, fourth)
        if fourth > 2*first:
            return False
        else:
            return True
        
