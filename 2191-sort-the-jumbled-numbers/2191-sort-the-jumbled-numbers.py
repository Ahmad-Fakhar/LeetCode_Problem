class Solution:

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map_value(num):
            return int("".join(str(mapping[int(digit)]) for digit in str(num)))
        
        mapped_values = [(map_value(num), i, num) for i, num in enumerate(nums)]
        mapped_values.sort()
        
        return [num for _, _, num in mapped_values]
   