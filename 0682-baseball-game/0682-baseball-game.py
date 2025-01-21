class Solution:
    def calPoints(self, operations: List[str]) -> int:
        Record = []
        for char in operations:
            if char == "+":
                Record.append(Record[-1]+Record[-2])
            elif char == "D":
                Record.append(Record[-1]*2)
            elif char == "C":
                Record.pop()
            else:
                Record.append(int(char))
        return sum(Record)
        