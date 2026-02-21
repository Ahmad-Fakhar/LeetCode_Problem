class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        cntPrimeSetBits = 0
        
        magicMask = 665772

        for num in range(left, right + 1):
        
            if (magicMask >> num.bit_count()) & 1:
                cntPrimeSetBits += 1

        return cntPrimeSetBits