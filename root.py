
def root(x, n):
  start = 0.0
  end = x
  while abs(end-start) > 0.001:
    mid = start + (end-start)/2.0
    print("mid", mid)
    # x = 9, mid = 4.5, n = 2
    #  16 > 9, end = 4, start = 0
    if pow(mid, n) > x:
      end = mid
    else:
      start = mid
  return start


print(root(9,2))   

