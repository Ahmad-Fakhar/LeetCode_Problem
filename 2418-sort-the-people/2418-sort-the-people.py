class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        paired = list(zip(names, heights))
        paired_sorted = sorted(paired, key=lambda x: x[1], reverse=True)
        sorted_names = [name for name, height in paired_sorted]
        return sorted_names