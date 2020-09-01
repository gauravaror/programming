def meeting_planner(slotsA, slotsB, dur):
  #slotsA = [[10, 50], [60, 120], [140, 210]]
  #slotsB = [[0, 15], [60, 70]]
  #   start 0, end =15
  #   min(15)
  # start1=10, start2 = 0, end1 = 15, end2 = 50
  # min(end1,end2) - max(start1, start2)
  #input:  slotsA = [[10, 50], [60, 120], [140, 210]]
  #      slotsB = [[0, 15], [60, 70]]

  #dur = 8
  #slotsA = [[10, 50], [60, 120]]
  #slotsB = [[0, 15], [42, 66]]
  # ans = [[42,50]]
  
  if len(slotsA) == 0 or len(slotsB) == 0:
    return []

  indA = 0
  indB = 0
  while indA < len(slotsA) and indB < len(slotsB):
    startB, endB = slotsB[indB]
    startA, endA = slotsA[indA]
    start = max(startA, startB)
    end = min(endA, endB)
    if end - start >= dur:
      return [start, start+dur]
    if endB < endA:
      indB += 1
    else:
      indA += 1
  return []
