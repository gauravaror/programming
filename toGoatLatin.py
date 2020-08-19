class Solution:
    def toGoatLatin(self, S: str) -> str:
        if len(S) == 0:
            return S
        vowels = ['a', 'i', 'o', 'u', 'e', 'A', 'I', 'O', 'U', 'E']
        words = S.split(' ')
        suffix = 'a'
        for idx in range(len(words)):
            word = words[idx]
            if len(word) == 0:
                del words[idx]
                continue
            if word[0] not in vowels:
                word = word[1:] + word[0]
            word += 'ma'
            word += suffix
            words[idx] = word
            suffix += 'a'
        return ' '.join(words)
