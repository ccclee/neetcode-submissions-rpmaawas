class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_count = {}
        start = 0
        max_length = 0
        for end in range(len(s)):
            char = s[end]
            char_count[char] = char_count.get(char, 0) + 1
        
            while char_count[char] > 1:
                char_count[s[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length

        