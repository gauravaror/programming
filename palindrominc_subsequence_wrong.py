class Solution:
    def removePalindromeSub(self, s: str) -> int:
        len_str =  len(s)
        dp = [[-1]*len_str for _ in range(len_str)]
        for i in range(len_str):
            dp[i][i] = 1
        def is_palindron(stri,start, end):
            length = end-start
            if length == 1:
                return True
            middle = start+ length//2
            offset = 0
            if not length % 2 == 0:
                offset = 1
            print("pieces", length, offset,  stri[start:middle] , stri[middle+offset:end])
            if stri[start:middle] == stri[middle+offset:end][::-1]:
                return True
            else:
                return False
        def remove_largest_pali(stri):
            print(stri)
            stri_len = len(stri)
            for i in range(0,stri_len//2+1):
                print(i, stri_len, stri[i:stri_len], stri[0:stri_len-i])
                if is_palindron(stri, i, stri_len):
                    stri = stri[:i]
                    print("Yes palidon ", stri)
                    break
                elif is_palindron(stri, 0,stri_len-i):
                    stri = stri[stri_len-i:]
                    print("Yes palidon ", stri)
                    break
            return stri
        step = 0
        while len(s) > 0:
            s = remove_largest_pali(s)
            step += 1
        return step
