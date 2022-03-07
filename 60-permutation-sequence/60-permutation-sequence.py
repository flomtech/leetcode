
class Solution:
    def getPermutation(self, n, k):
        assert 1 <= n <= 9
        tt = 1
        for i in xrange(n):     tt *= i + 1
        k = k - 1
        assert 0 <= k < tt
        res = []                     
        c = range(1, n+1)     
        rem = tt       
        for p in xrange(n, 0, -1):
            rem = rem // p
            res.append(str(c[k//rem]))
            c.remove(c[k//rem])
            k %= rem
        return "".join(res)