import sys



def run_program(list_codes):
        for i in range(0, len(list_codes), 4):
            current_op = int(list_codes[i])
            if current_op == 99:
                return list_codes
            first_one = list_codes[int(list_codes[i+1])]
            second_one = list_codes[int(list_codes[i+2])]
            output = first_one + second_one
            if current_op == 2:
                output = first_one*second_one
            position_rep = int(list_codes[i+3])
            list_codes[position_rep] = output

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        given_input = f.readline()
        print("Given input", given_input)
        given_input = given_input.strip()
        list_codes = [ int(g) for g in given_input.split(',')]
        for i in range(100):
            for j in range(100):
                try_list = list_codes.copy()
                try_list[1] = i
                try_list[2] = j
                out = run_program(try_list)
                #print("Trying ", i, j, out[0])
                if (19690720 == out[0]):
                    print("i ", i, "j", j, "output", 100*i + j)
                    #sys.exit(0)

