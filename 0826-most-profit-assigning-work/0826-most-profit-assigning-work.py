class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        
        # Sort the worker array
        worker.sort()
        
        #Traverse through workers and find the best possible job they can complete
        max_profit = 0
        job_index = 0
        best_profit = 0
        
        for ability in worker:
            # Move the job index to the most profitable job that the current worker can complete
            while job_index < len(jobs) and jobs[job_index][0] <= ability:
                best_profit = max(best_profit, jobs[job_index][1])
                job_index += 1
            
            max_profit += best_profit
        
        return max_profit