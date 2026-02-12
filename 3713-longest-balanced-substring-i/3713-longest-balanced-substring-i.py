class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 0

        i = 0
        while(i < len(s)):
            
            occr_dict = dict()
            j = i
            while(j < len(s)):
                
                if(s[j] not in occr_dict):
                    occr_dict[s[j]] = 1
                else:
                    occr_dict[s[j]] += 1

                if(len(set(occr_dict.values())) == 1):
                    ans = max(ans, j - i + 1) 


                j += 1
            i += 1
        
        return ans