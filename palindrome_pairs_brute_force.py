class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(first, second):
            word = first + second
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
            
            
            
        pairs = []
        for idx,i in enumerate(words):
            for jdx,j in enumerate(words):
                if idx == jdx:
                    continue
                if is_palindrome(i,j):
                    pairs.append([idx,jdx])
        return pairs 
