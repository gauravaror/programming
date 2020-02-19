def missingWords(s, t):
    original = s.split()
    substring = t.split()
    o_id = 0
    sub_id = 0
    miss = []
    while(o_id < len(original)):
        if sub_id < len(substring) and original[o_id] == substring[sub_id]:
            o_id += 1
            sub_id += 1
        else:
            miss.append(original[o_id])
            o_id += 1
    return miss

assert missingWords("I like cheese", "like") == ["I", "cheese"]
assert missingWords("I am using HR to improve programming", "am HR to improve") == ["I", "using", "programming"]

