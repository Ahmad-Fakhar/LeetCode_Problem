class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # If the number is greater than the target, break since further numbers will also be too large
                if candidates[i] > target:
                    break
                # Include the candidate and move to the next one
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])
        
        candidates.sort()  # Sort the candidates to handle duplicates and improve efficiency
        result = []
        backtrack(0, target, [])
        return result