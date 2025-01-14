class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        element_map = {}
        ans = []
        common_count = 0

        for i in range(len(A)):
            # Process element from array A
            if A[i] not in element_map:
                element_map[A[i]] = [True, False]
            else:
                if not element_map[A[i]][0] and element_map[A[i]][1]:
                    common_count += 1
                    element_map[A[i]][0] = True

            # Process element from array B
            if B[i] not in element_map:
                element_map[B[i]] = [False, True]
            else:
                if not element_map[B[i]][1] and element_map[B[i]][0]:
                    common_count += 1
                    element_map[B[i]][1] = True

            # Append the count of common elements to the result
            ans.append(common_count)

        return ans