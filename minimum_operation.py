current_table = {}

def minimum_operation(end=10):
    if end in current_table:
        return current_table[end]
    if end % 2 == 0:
        oper1 = end // 2
    else:
        oper1 = -1
    oper2 = end - 1

    if oper1 == 0 or oper2 == 0:
        current_table[end] = 1
        return 1
    else:
        output2 = end
        output1 = end
        if oper2 > 0:
            output2 = 1 + minimum_operation(oper2)
        if oper1 > 0:
            output1 = 1 + minimum_operation(oper1)
        if output2 < output1:
            current_table[end] = output2
            return output2 
        else:
            current_table[end] = output1
            return output1 

assert minimum_operation(8) ==  4
assert minimum_operation(7) == 5


if __name__ == "__main__":
    input_ = input()
    for _ in range(int(input_)):
        N = int(input())
        print(minimum_operation(end=N))
