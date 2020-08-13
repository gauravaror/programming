class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        output = [""]
        for char in characters:
            output.extend([i+char for i in output])
        print(output)
        self.output = list(filter(lambda x: len(x) == combinationLength, output))
        self.output = sorted(self.output)
        print(self.output)
        self.index = 0
        

    def next(self) -> str:
        if self.index <= len(self.output)-1:
            out = self.output[self.index]
            self.index += 1
            return out
        else:
            return -1
            

    def hasNext(self) -> bool:
        print(self.index)
        if self.index <= len(self.output)-1:
            return True
        return False
        
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
