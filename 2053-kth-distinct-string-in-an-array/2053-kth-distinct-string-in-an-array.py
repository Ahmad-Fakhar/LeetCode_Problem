class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
                
        # Step 1: Count occurrences of each string
        count = Counter(arr)
        
        # Step 2: Collect distinct strings
        distinct_strings = [string for string in arr if count[string] == 1]
        
        # Step 3: Return the kth distinct string if it exists
        if k <= len(distinct_strings):
            return distinct_strings[k - 1]
        else:
            return ""