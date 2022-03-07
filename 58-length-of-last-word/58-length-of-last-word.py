class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        l=len(s.split()[-1])
        if l == -1:
            return 0
        return l