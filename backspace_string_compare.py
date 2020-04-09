class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def get_string_representation(S):
            pending_backspace = 0
            output = []
            for i in S:
                if i == '#':
                    pending_backspace += 1
                else:
                    output_len = len(output)
                    for j in range(pending_backspace):
                        remove_char = output_len - j - 1
                        if len(output) == 0:
                            pending_backspace = 0
                            break
                        del output[remove_char]
                    pending_backspace = 0
                    output.append(i)
            if pending_backspace > 0:
                output_len = len(output)
                for j in range(pending_backspace):
                    remove_char = output_len - j - 1
                    del output[remove_char]
                    if len(output) == 0:
                        break
            print(output)
            return ''.join(output)
        if get_string_representation(S) == get_string_representation(T):
            return True
        else:
            return False
