# coding: utf-8
import math
import string
from collections import Counter
def solution(T, R):
    correct = Counter()
    wrong = Counter()
    for name,test in zip(T,R):
        gname = name[:-1] if name[-1] in string.ascii_lowercase else name
        if test == 'OK':
            correct[gname] += 1
        else:
            wrong[gname] += 1
    correct_group  = 0
    total_group = set(list(correct.keys()) + list(wrong.keys()))
    for key in total_group:
        if key in correct and key not in wrong:
            correct_group += 1
    return math.floor(correct_group*100/len(total_group))
            
        
