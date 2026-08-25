class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        longest_str = 1
        if s == "":
            return 0
        curr = s[0]
        while(j < len(s)):
            curr = s[i:j]
            if s[j] in curr:
                i += 1
            else:
                curr += s[j]
                longest_str = max(longest_str, len(curr))
                j += 1
        return longest_str  