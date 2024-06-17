class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0:
            return False

        # Function to check if a number is of the form 4k + 3
        def is_4k_plus_3(n):
            return n % 4 == 3
        
        # Factorize c and check exponents of primes of the form 4k+3
        for i in range(2, int(math.sqrt(c)) + 1):
            if c % i == 0:
                count = 0
                while c % i == 0:
                    c //= i
                    count += 1
                if is_4k_plus_3(i) and count % 2 != 0:
                    return False
        
        # If c is a prime factor greater than 1 at the end, check it as well
        if c > 1 and is_4k_plus_3(c):
            return False
        
        return True
        