class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        processed = [ i-j for i,j in zip(gas, cost) ]
        cache = {}
        def maxReach(petrol, i, starting):
            #print("MRS", petrol,i,starting)
            if petrol < 0:
                return -1
            if i == starting:
                return starting
            if (petrol,i) in cache:
                return cache[(petrol,i)]
            if i in cache:
                oldpetrol, oldi = cache[i]
                if petrol > oldpetrol:
                    npetrol = petrol - oldpetrol
                    #i = oldi
                    newreach = maxReach(npetrol, oldi, starting)
                    cache[i] = (petrol, newreach)
                    cache[(petrol,i)] = newreach
                    return newreach
                if petrol < oldpetrol and starting >= oldi:
                    return -1
            nex =  (i+1)%len(gas)
            out = maxReach(petrol + processed[i], nex, starting)
            if out == -1:
                canreach = i
            else:
                canreach = out
                cache[i] = (petrol, out)
                cache[(petrol,i)] = out
            #print("MRE", petrol, i, canreach)
            return out
        #print(processed)
        for idx,i in enumerate(processed):
            if i >= 0:
                #print("calling", i, idx)
                reach = maxReach(i, (idx+1)%len(gas), idx)
                if reach == idx:
                    return reach
        #print(cache)
        return -1
