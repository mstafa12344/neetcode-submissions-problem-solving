class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            visited = set()
            currentLen = 0
            for j in range(i,len(s)):
                if s[j] in visited:
                    break
                visited.add(s[j])
                currentLen +=1
            max_len = max(currentLen,max_len)

        return max_len
