class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        # Define the lists for units, teens, and tens
        units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def three_digit_number_to_words(n):
            hundred = n // 100
            rest = n % 100
            result = ""

            if hundred != 0:
                result += units[hundred] + " Hundred"
            
            if rest != 0:
                if result != "":
                    result += " "
                if rest < 10:
                    result += units[rest]
                elif 10 <= rest < 20:
                    result += teens[rest - 10]
                else:
                    ten = rest // 10
                    unit = rest % 10
                    result += tens[ten]
                    if unit != 0:
                        result += " " + units[unit]
            
            return result

        result = ""
        thousand_index = 0

        while num > 0:
            if num % 1000 != 0:
                result = three_digit_number_to_words(num % 1000) + " " + thousands[thousand_index] + " " + result
            num //= 1000
            thousand_index += 1

        return result.strip()
        