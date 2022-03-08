class Solution:
    def wordBreak(self, s, words):
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in words:
                k = i - len(word)
                if word == s[k + 1:i + 1] and (dp[k] or k == -1):
                    dp[i] = True
        return dp[-1]