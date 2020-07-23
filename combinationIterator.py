class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.sol = [[]]
        for i in characters:
            self.sol.extend([s + [i] for s in self.sol])
        self.output = []
        for i in self.sol:
            if len(i) == combinationLength:
                self.output.append(i)
        self.output.sort()
        self.len = len(self.output)
        self.curr = 0
        

    def next(self) -> str:
        if self.curr >= self.len:
            return ''
        s = self.output[self.curr]
        self.curr += 1
        return ''.join(s)
    
        
    def hasNext(self) -> bool:
        if self.curr >= self.len:
            return False
        else:
            return True
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
