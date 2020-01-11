class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(word):
            w_len = len(word)
            if w_len == 1:
                return True
            if w_len == 0:
                return False
            if w_len % 2 != 0:
                right_index = w_len//2 - 1
                left_index = w_len//2 + 1
            else:
                right_index = w_len//2
                left_index = right_index - 1
            
            while ( left_index >=0 and right_index < w_len):
                if not (word[left_index] == word[right_index]):
                    return False
                right_index += 1;
                left_index -= 1;
            if (left_index == -1) and (right_index == w_len):
                return True
            else:
                return False
            
        hash_table = {word: i for i,word in enumerate(words)}
        palindroms = [idx for idx,word in enumerate(words) if is_palindrome(word)]
        pairs = []
        for idx,i in enumerate(words):
            if len(i) == 0:
                for pal_indx in palindroms:
                    if idx != pal_indx:
                        pairs.append([idx, pal_indx])
            reverse_word = i[::-1]
            if reverse_word in hash_table:
                palindrom = hash_table[reverse_word]
                if palindrom != idx:
                    pairs.append([idx, palindrom])
            for pidx,j in enumerate(i):
                suffix = i[:pidx]
                prefix = i[pidx:]
                if is_palindrome(suffix) and prefix[::-1] in hash_table:
                    nid = hash_table[prefix[::-1]]
                    if nid != idx:
                        pairs.append([nid, idx])
                if is_palindrome(prefix) and suffix[::-1] in hash_table:
                    nid = hash_table[suffix[::-1]]
                    if nid != idx:
                        pairs.append([idx, nid])
                    
        return pairs
