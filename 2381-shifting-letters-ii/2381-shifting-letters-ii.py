import numpy as np

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        n = len(s)
        shift = np.zeros(n)

        for l, r, d in shifts:
            if d == 0:
                shift[l:r+1] -= 1
            else:
                shift[l:r+1] += 1

        s = list(s)

        for i in range(n):
            s[i] = self.shift_char(s[i], int(shift[i]))

        return ''.join(s)
    
    def shift_char(self, char, shift):

         return chr(97 + ((ord(char) - 97) + shift) % 26)