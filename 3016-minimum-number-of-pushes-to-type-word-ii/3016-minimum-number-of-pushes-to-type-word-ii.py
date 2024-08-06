class Solution:
    def minimumPushes(self, word: str) -> int:
            # Create a list to hold the frequency of each letter (26 letters)
        mp = [0] * 26
        
        # Count the frequency of each letter in the word
        for ch in word:
            mp[ord(ch) - ord('a')] += 1  # Convert char to index (0-25)
        
        # Sort the frequency list in descending order
        mp.sort(reverse=True)
        
        # Calculate the minimum number of presses
        ans = 0
        for i in range(26):
            ans += mp[i] * ((i // 8) + 1)
        
        return ans