class Codec:

    def __init__(self):
        self.storage = []
        self.conversion =  string.ascii_lowercase + string.ascii_uppercase + "0123456789"
        self.base = len(self.conversion)
        
    def encode(self, longUrl: str) -> str:
        index = len(self.storage)
        self.storage.append(longUrl)
        if index < self.base:
            return self.conversion[index]
        output = ""
        while index > self.base:
            output += self.conversion[index % self.base]
            index = index//self.base
        return output[::-1]
            

    def decode(self, shortUrl: str) -> str:
        num = 0
        for i in shortUrl:
            num = num*62 + self.conversion.index(i)
        print(num, self.storage, shortUrl)
        return self.storage[num]
            
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
