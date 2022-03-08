from itertools import zip_longest
class Solution:    
    def isIsomorphic(self,a, b):
        f = a
        s = b
        return len(set(f)) == len(set(s)) == len(set(zip_longest(f, s)))