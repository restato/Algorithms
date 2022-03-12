# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def checkPalindrome(self,s, l, r):
        while(l>=0 and r<len(s) and s[l]==s[r]):
            l-=1;
            r+=1;
        return(r-l-1)
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        res = ""
        for i in range(len(s)):
            len1 = self.checkPalindrome(s,i,i)
            len2 = self.checkPalindrome(s,i,i+1)
            leng = max(len1,len2)
            if(leng>end-start):
                start = i-(leng-1)//2
                end = i+leng//2
                res = s[start:end+1]
        return(res)
