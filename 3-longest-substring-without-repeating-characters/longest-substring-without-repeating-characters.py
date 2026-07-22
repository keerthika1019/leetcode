class Solution:
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1

            char_index[s[right]] = right
            ans = max(ans, right - left + 1)

        return ans