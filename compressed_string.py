#!/bin/python

def decompress_string(text):
    current_num = 0
    input_string = ""
    open_brackets = 0
    output_string = ""
    for i in text:
        if i == ']':
            if open_brackets == 1:
                #print("calling input_string on ", input_string)
                return_value = decompress_string(input_string)
                output_string +=  current_num*return_value
                open_brackets = 0
                input_string = ""
                current_num = 0
            else:
                input_string += i
                open_brackets -= 1

        elif (open_brackets == 0) and ord(i) < 58 and ord(i) > 47:
            current_num = current_num*10 + int(i)
        elif i == '[':
            if open_brackets > 0:
                input_string += i
            open_brackets += 1
        elif open_brackets == 0:
            output_string += i
        else:
            #print(i, input_string)
            input_string += i
    return output_string


assert decompress_string("3[a]") ==  "aaa"
assert decompress_string("0[a]") ==  ""
assert decompress_string("12[a]") ==  "aaaaaaaaaaaa"
assert decompress_string("12[a]3[b]") ==  "aaaaaaaaaaaabbb"
assert decompress_string("100[]") ==  ""
assert decompress_string("abc3[b]") == "abcbbb"
assert decompress_string("cd2[2[ab]]gd") == "cdababababgd"
assert decompress_string("cd2[2[ab]]gd3[ab]") == "cdababababgdababab"
assert decompress_string("3[abc]4[ab]c") == "abcabcabcababababc"
assert decompress_string("2[3[a]b]") == "aaabaaab"
assert decompress_string("a[]b") == "ab"
assert decompress_string("0[abc]") == ""
