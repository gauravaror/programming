# 7, 3
# 1, 7
#   pow(4,3) > 7
# end = 4, start 0
# mid = 2
# end = 2, start = 0
# start = 1, end = 2
# mid = 1.5
# 0.9 --- powe(0.9,3) < 0.9
# x = 0.09 ,  n = 2, 0.3
# start = 0 , end = 0.09, mid = 0.045
# 0.045^2 < 0.045
# 0.002025 < x rig
# 0.0001 
# https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems


def root(x, n):
  start = 0.0
  end = x
  if x ==0:
    return 0
  if x < 1:
    end = 1  
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


print(root(0.3,2))   

