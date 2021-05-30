class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convert(data):
            word = ""
            for w in data:
                word += str(string.ascii_lowercase.index(w))
            return int(word)
        f = convert(firstWord)
        s = convert(secondWord)
        t = convert(targetWord)
        return f+s == t
