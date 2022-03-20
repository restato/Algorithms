# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution: 
    def lengthOfLongestSubstring(self, s):
        start = 0 # 반복 없었던 character의 시작 위치
        max_length = 0
        used = {} # save location of char
        
        '''
        char: t, start: 0, max_length: 0
        char: m, start: 0, max_length: 1
        char: m, start: 0, max_length: 2
        start: 0 used[s[i]]: 1
        char: z, start: 2, max_length: 2
        char: u, start: 2, max_length: 2
        char: x, start: 2, max_length: 3
        char: t, start: 2, max_length: 4
        
        # start <= used[s[i]] 가 없는 경우 오류
        char: t, start: 0, max_length: 0
        char: m, start: 0, max_length: 1
        char: m, start: 0, max_length: 2
        start: 0 used[s[i]]: 1
        char: z, start: 2, max_length: 2
        char: u, start: 2, max_length: 2
        char: x, start: 2, max_length: 3
        char: t, start: 2, max_length: 4 <-- t가 이전에 0번에서 등장했는데 이미 시작은 2번부터
        start: 2 used[s[i]]: 0
        '''
        
        for i in range(len(s)):
            print(f'char: {s[i]}, start: {start}, max_length: {max_length}')
            # start <= used[s[i]]:
            # start: max_length를 계산할때 시작하는 index (=반복된적 없었던 단어의 시작 index)
            # used[s[i]]: 이전에 등장했던 char
            if s[i] in used: and start <= used[s[i]]: # 🔑
                print(f'start: {start} used[s[i]]: {used[s[i]]}')
                start = used[s[i]] + 1 # 이전에 등장했으면 시작을 다음으로 변경
            else:
                max_length = max(max_length, i - start + 1) # 🔑
            used[s[i]] = i # 🔑
        return max_length
