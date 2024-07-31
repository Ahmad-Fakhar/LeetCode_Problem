class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s_list = list(s)  # Convert the string to a list to allow mutability
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move the left pointer until a vowel is found
            if s_list[left] not in vowels:
                left += 1
            # Move the right pointer until a vowel is found
            elif s_list[right] not in vowels:
                right -= 1
            # If both pointers are at vowels, swap and move both pointers inward
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
                
        return ''.join(s_list)  # Convert the list back to a string
