class Solution(object):
    def lengthOfLongestSubstring(self, s):
        freq = {}
        left = 0
        longest_substring = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0) + 1

            k = right-left+1

            while len(freq) < k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
                k = right-left+1
            
            longest_substring = max(longest_substring,right-left+1)
            


        return longest_substring