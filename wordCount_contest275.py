class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def get_code(word, ignore=None):
            rcode = ["0"]*26
            for idx, i in enumerate(word):
                if ignore != None and idx == ignore:
                    continue
                rcode[string.ascii_lowercase.index(i)] = "1"
            return ''.join(rcode)
        h = {}
        for i  in startWords:
            h[get_code(i)] = True

        can_do = 0
        #print(h)
        for word in targetWords:
            for idx, i in enumerate(word):
                #print(word, idx, get_code(word, idx))
                if get_code(word, idx) in h:
                    can_do += 1
                    break
        return can_do
