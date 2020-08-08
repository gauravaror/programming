def solution(inp, dic):
    def back(st, dic, last_space, pos):
        if len(st) == pos:
            print(st, st[last_space:pos+1], st[last_space:pos+1] in dic)
            if st[last_space:pos+1] in dic:
                return [st]
            else:
                return []
        if st[pos] == ' ':
            output = []
            if st[last_space:pos] in dic:
                a1 = back(st, dic, pos+1, pos+1)
                if a1:
                    output.extend(a1) 
            a2 = back(st[:pos] + 'e' + st[pos+1:], dic, last_space, pos +1)
            if a2:
                output.extend(a2)
            return output
        else:
            return back(st, dic, last_space, pos+1)
    return back(inp, dic, 0, 0)

print(solution("can s r n ", ["can", "canes", "serene", "rene", "sam"]))
