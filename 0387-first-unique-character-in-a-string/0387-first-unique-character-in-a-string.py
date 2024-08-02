class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Count character frequencies
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Step 2: Find the first non-repeating character
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        
        # If no non-repeating character exists
        return -1