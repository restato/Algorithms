# https://leetcode.com/problems/word_break/

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
        dp = [False] * (len(s) + 1) 
        dp[0] = True
        for i in range(len(s)):
            # print(dp[i])
            if dp[i]:
                for j in range(i + 1, len(s) + 1):
                    # print(s[i:j])
                    if s[i:j] in wordDict:
                        # print('hit', j)
                        dp[j] = True # 🔑 hit된 마지막 인덱스를 저장해 이전은 확인 안하도록 e.g., applepenapple 의 경우 apple은 다시 체크할 필요 없이 pen 부터 확인
        return dp[-1]
