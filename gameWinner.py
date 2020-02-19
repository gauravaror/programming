def gameWinner(colors):
    length = len(colors)
    start=0
    end = 0
    current_character = colors[start]
    current_seq = 1
    total_each = {'w': 0, 'b':0}
    while end< length:
        if colors[end] == current_character:
            current_seq += 1
        else:
            this_seq = end - start
            total_each[current_character] += (this_seq-2)
            start=end
            current_character = colors[start]
        end += 1
    this_seq = end-start
    total_each[current_character] += (this_seq-2)
    print("ta", total_each['b'], total_each['w'])
    if total_each['b'] > total_each['w']:
        return "bob"
    elif total_each['w'] > total_each['b']:
        return "wendy"
    else:
        return "bob"
print(gameWinner("wwwbb"))
assert gameWinner("wwwbb") == "wendy"
assert gameWinner("wwwbbbbwww") == "bob"
assert gameWinner("wwwwbbbbwww") == "wendy"
assert gameWinner("wb") == "bob"
            

