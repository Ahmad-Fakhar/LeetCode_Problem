class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
          # Define the boundaries of 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX  # because abs(INT_MIN) exceeds INT_MAX
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with absolute values to avoid negative complications
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Quotient to store the result
        quotient = 0
        
        # We will use bit shifting to optimize the subtraction process
        while dividend >= divisor:
            temp_divisor, num_shifts = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_shifts <<= 1
            
            # Subtract the largest shifted divisor
            dividend -= temp_divisor
            quotient += num_shifts
        
        # Apply the sign to the quotient
        if negative:
            quotient = -quotient
        
        # Clamp the result within the 32-bit integer range
        return max(INT_MIN, min(INT_MAX, quotient))