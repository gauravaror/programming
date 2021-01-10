class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        encoded.insert(0, first)
        print(encoded)
        for i in range(1,len(encoded)):
            encoded[i] = encoded[i] ^ encoded[i-1]
        return encoded
            
        
