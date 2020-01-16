class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        print(A, B)
        def find_all_positions(num: int):
            pos  = []
            for idx,i in enumerate(B):
                if num == i:
                    pos.append(idx)
            return pos
        starting_positions = []
        max_seq_length = 0
        curr_seq_length = 0
        for ikx,k in enumerate(A):
            #print("Running", k, ikx)
            curr_seq_length = 0
            starting_positions = find_all_positions(k)
            if len(starting_positions) > 0:
                curr_seq_length = 1
                if curr_seq_length > max_seq_length:
                    max_seq_length = curr_seq_length
            for j in A[ikx+1:]:
                #print(j, starting_positions, curr_seq_length)
                if len(starting_positions) == 0:
                    break
                else:
                    temp_positions = []
                    any_match = False
                    for pos in starting_positions:
                        if pos + 1 < len(B):
                            #print("Matching ", j, pos+1, B[pos+1])
                            if B[pos+1] == j:
                                #curr_seq_length += 1
                                any_match = True
                                temp_positions.append(pos + 1)
                    if any_match:
                        curr_seq_length += 1
                    starting_positions = temp_positions

                if curr_seq_length > max_seq_length:
                    max_seq_length = curr_seq_length
        return max_seq_length
