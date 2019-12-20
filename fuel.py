import sys
import math

def fuel_required(required_fuel: int):
    current_requirement = (math.floor(int(required_fuel)/3) - 2)
    if current_requirement > 0:
        to_load = fuel_required(current_requirement)
        return to_load + current_requirement
    else:
        return 0

if __name__ == "__main__":
    print(sys.argv[1])
    with open(sys.argv[1]) as f:
        sum_var = 0
        for line in f.readlines():
            line.strip()
            sum_var += fuel_required(int(line))
        print("Sum is ", sum_var)
