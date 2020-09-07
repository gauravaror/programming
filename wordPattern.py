class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(' ')
        mappings = {}
        mapped_words = set()
        if not pattern:
            return False
        if len(pattern) != len(words):
            return False
        for letter,word in zip(pattern, words):
            if letter in mappings:
                if word != mappings[letter]:
                    return False
            else:
                if word not in mapped_words:
                    mappings[letter] = word
                    mapped_words.add(word)
                else:
                    return False
        return True
