class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s: str, sub: str, points: int) -> (str, int):
            stack = []
            point_total = 0
            
            for char in s:
                stack.append(char)
                if len(stack) >= 2 and stack[-2] + stack[-1] == sub:
                    stack.pop()  # remove the last character
                    stack.pop()  # remove the second last character
                    point_total += points  # add points
            
            return ''.join(stack), point_total
        if x >= y:
            s, points_ab = remove_substring(s, "ab", x)
            s, points_ba = remove_substring(s, "ba", y)
        else:
            s, points_ba = remove_substring(s, "ba", y)
            s, points_ab = remove_substring(s, "ab", x)

        return points_ab + points_ba