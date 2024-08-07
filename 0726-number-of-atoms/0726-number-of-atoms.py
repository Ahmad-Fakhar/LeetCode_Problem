class Solution:
    import collections
    def countOfAtoms(self, formula: str) -> str:
        
        def parse():
            N = len(formula)
            i = 0
            stack = [collections.Counter()]
            
            while i < N:
                if formula[i] == '(':
                    stack.append(collections.Counter())
                    i += 1
                elif formula[i] == ')':
                    top = stack.pop()
                    i += 1
                    i_start = i
                    while i < N and formula[i].isdigit():
                        i += 1
                    multiplicity = int(formula[i_start:i] or 1)
                    for name, v in top.items():
                        stack[-1][name] += v * multiplicity
                else:
                    i_start = i
                    i += 1
                    while i < N and formula[i].islower():
                        i += 1
                    name = formula[i_start:i]
                    i_start = i
                    while i < N and formula[i].isdigit():
                        i += 1
                    multiplicity = int(formula[i_start:i] or 1)
                    stack[-1][name] += multiplicity
            
            return stack[0]
        
        counts = parse()
        output = []
        for name in sorted(counts):
            output.append(name)
            if counts[name] > 1:
                output.append(str(counts[name]))
        
        return "".join(output)