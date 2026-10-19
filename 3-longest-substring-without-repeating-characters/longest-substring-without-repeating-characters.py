class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mpp = {}
        left = 0 
        max_len = 0 
        for right in range(len(s)):
            ch = s[right]

            if ch in mpp :
                left = max(left,mpp[ch]+1)
            mpp[ch] = right 

            max_len = max(max_len,right - left + 1)

        return max_len
