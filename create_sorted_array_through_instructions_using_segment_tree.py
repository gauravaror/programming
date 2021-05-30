class Solution:
    # Python3 Code Addition 

    # limit for array size  
    N = 100000;  

    # Max size of tree  
    tree = [0] * (2 * N);  

    # function to update a tree node  
    def updateTreeNode(self, p, value, n) :  

        # set value at position p  
        self.tree[p + n] = value;  
        p = p + n;  

        # move upward and update parents  
        i = p; 

        while i > 1 : 

            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1];  
            i >>= 1;  

    # function to get sum on interval [l, r)  
    def query(self, l, r, n) :  

        res = 0;  

        # loop to find the sum in the range  
        l += n; 
        r += n; 

        while l < r : 

            if (l & 1) : 
                res += self.tree[l];  
                l += 1

            if (r & 1) : 
                r -= 1; 
                res += self.tree[r];  

            l >>= 1; 
            r >>= 1

        return res;  

    def createSortedArray(self, instructions: List[int]) -> int:
        #print("ins", instructions)
        c = Counter()
        cost = 0
        len_ins = len(instructions)
        for idx,i in enumerate(instructions):
            less = self.query(0, i-1, len_ins)
            equal = c[i]
            print("Less Equal", less, equal, cost)
            cost += min(less, idx-less-equal)
            self.updateTreeNode(i, equal + 1,  len_ins)
            c[i] += 1
        return cost % (10**9 + 7)


