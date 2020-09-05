# source = "
# words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
# bit - > ["but", "big"]
# [(bit,0)]
# [(but,1),(big,1)]
# ["dmd"]
# N^2 operation.
# breath first search
def shortestWordEditPath(source, target, words):
	"""
	@param source: str
	@param target: str
	@param words: str[]
	@return: int
	"""
  def oneDistance(word1, word2):
    num_diff = 0
    for w1,w2 in zip(word1, word2):
      if w1 != w2:
        num_diff +=  1
    return num_diff == 1
  
  edge_list = defaultdict(list)
  new_wordlist = [source] + words
  for i in range(len(new_wordlist)):
    for j in range(i+1,len(new_wordlist)): ### ['ab','dc']
      if oneDistance(new_wordlist[i], new_wordlist[j]):
        edge_list[new_wordlist[i]].append(new_wordlist[j])
        edge_list[new_wordlist[j]].append(new_wordlist[i])
  queue = deque()
  seen = set()
  seen.add(source)
  queue.append([(source, 0)])
  while len(queue) > 0:
    elem, plen = queue.pop_left() # (bil,1)
    if elem == target:
      return plen + 1
    if elem in edge_list: # source = "bit" ... words = ["bil", "afs", "big"] , target = "big" 
      for i in edge_list[elem]:
        if i not in seen:
          seen.add(i)
          queue.append((i, plen+1)) # (1,bil)
  return -1
  # Run time complexity : O(N^2*M)  --> N = Number of words in words list, and M = len(source) string
  # space : O(N^2)
  # big: *ig , b*g, bi* hash [*ig] => [big, but, bit, ] # 26 chara  N.M
    
    

