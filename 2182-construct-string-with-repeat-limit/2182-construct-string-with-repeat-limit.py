class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Frequency array to store character counts
        count = [0] * 26
        
        # Count the frequency of each character
        for ch in s:  # T.C: O(n)
            count[ord(ch) - ord('a')] += 1
        
        # Max heap to store characters in descending order
        max_heap = []
        for i in range(26):
            if count[i] > 0:
                heappush(max_heap, (-i, chr(i + ord('a'))))  # Push as a tuple of (-index, character)

        result = []

        while max_heap:
            _, ch = heappop(max_heap)  # Get the largest character
            freq = min(count[ord(ch) - ord('a')], repeatLimit)  # Append up to 'repeatLimit' times
            
            for _ in range(freq):
                result.append(ch)
            count[ord(ch) - ord('a')] -= freq

            # If the current character still has remaining occurrences
            if count[ord(ch) - ord('a')] > 0 and max_heap:
                _, next_ch = heappop(max_heap)  # Get the next largest character
                result.append(next_ch)
                count[ord(next_ch) - ord('a')] -= 1

                # Reinsert characters into the priority queue if they still have remaining occurrences
                if count[ord(next_ch) - ord('a')] > 0:
                    heappush(max_heap, (-ord(next_ch) + ord('a'), next_ch))
                heappush(max_heap, (-ord(ch) + ord('a'), ch))

        return ''.join(result)
        