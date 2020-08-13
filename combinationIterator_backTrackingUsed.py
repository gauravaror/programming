class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.output = []
        def back(characters, st, first_char):
            #print(characters, st, first_char)
            if len(st) == combinationLength:
                self.output.append(st)
                return
            if first_char > len(characters) -1:
                return
            back(characters, st+characters[first_char], first_char+1)
            back(characters, st, first_char+1)
        back(characters,'', 0)
        #print(self.output)
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
