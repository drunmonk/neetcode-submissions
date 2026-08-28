class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch=set()
        l=0
        max_s=0
        for i in range(len(s)):
            while s[i] in ch:
                ch.remove(s[l])
                l+=1
            ch.add(s[i])
            max_s=max(max_s,i-l+1)
        return max_s
        