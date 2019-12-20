import sys
from typing import List, Callable


def read_input(input_file):
    with open(input_file) as f:
        return f.readline()


def digits(number: int, num_digit:int = 6) -> List[int]:
    digit = []
    for _ in range(num_digit):
        digit.append(number % 10)
        number = number // 10
    return list(reversed(digit))

assert digits(123456) == [1,2,3,4,5,6]
assert digits(2343) == [0,0,2,3,4,3]

def is_increasing(num: List[int]) -> bool:
    return all( i<=j for i,j in zip(num[:-1], num[1:]))

def same_adjacent(num: List[int]) -> bool:
    return any(i==j for i,j in zip(num[:-1], num[1:]))

assert is_increasing(digits(123455))
assert not is_increasing(digits(4324233))

assert not same_adjacent(digits(892987))
assert same_adjacent(digits(330694))

def is_valid(num: List[int]) -> bool:
    return is_increasing(num) and same_adjacent(num)


def two_group(num: List[int]) -> bool:
    for i,j in zip(list(range(6)),list(range(1,6))):
        if num[i] == num[j]:
            if i==0:
                if num[j+1] != num[j]:
                    return True
            elif j== (len(num) -1):
                if num[i-1] != num[i]:
                    return True
            else:
                if (num[i-1] != num[i]) and  (num[j+1] != num[j]):
                    return True

    return False


assert not two_group(digits(18786387))
assert two_group(digits(324233438))
assert not two_group(digits(32234233333))

def is_valid2(num: List[int]) -> bool:
    return is_increasing(num) and two_group(num)

def solve(input_file: str, func: Callable):
    line = read_input(input_file)
    input_range = line.split('-')
    start_input = input_range[0]
    end_input = input_range[1]
    return sum([ func(digits(i)) for i in range(int(start_input), int(end_input))])

if __name__ == "__main__":
    print("Part 1 ", solve(sys.argv[1], is_valid))
    print("Part 2 ", solve(sys.argv[1], is_valid2))

