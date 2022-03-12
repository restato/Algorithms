class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)-1):
            if (s[i] != s[i+1]) & (s[i].lower() == s[i+1].lower()):
                return self.makeGood(s[:i] + s[i+2:])
        return s
