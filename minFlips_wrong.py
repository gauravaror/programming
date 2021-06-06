class Solution:
    def minFlips(self, s: str) -> int:
        def distance(s, start = '0'):
            ds = 0
            distances = [0]*len(s)
            for idx,i in enumerate(s):
                if i != start:
                    ds += 1
                distances[idx] = ds
                start = '0' if start == '1' else '1'
            return ds, distances
        
        ds0, distances0 = distance(s, '0')
        ds1, distances1 = distance(s, '1')
        mina = len(s)
        for i in range(len(s)):
            even_right = (len(s) - i - 1) % 2 == 0
            even_left = (i + 1) == 0
            if even_right:
                ones = (distances1[-1] - distances1[i])
                zeros = (distances0[-1] - distances0[i])
                first = ones if even_left else zeros
                second = zeros if even_left else ones  
                first += distances1[i]
                second += distances0[i]

                mina = min(mina, min(first, second))
            else:
                ones = (distances1[-1] - distances1[i])
                zeros = (distances0[-1] - distances0[i])
                first = ones if even_left else zeros
                second = zeros if even_left else ones  
                first += distances0[i]
                second += distances1[i]
                mina = min(mina, min(first, second))
        return mina
            
                    
