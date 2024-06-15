class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Check if str1 + str2 == str2 + str1
        if str1 + str2 != str2 + str1:
            return ""

        # Find the greatest common divisor of the lengths of str1 and str2
        gcd_length = gcd(len(str1), len(str2))

        # The GCD string will be the prefix of str1 (or str2) with the length gcd_length
        return str1[:gcd_length]
