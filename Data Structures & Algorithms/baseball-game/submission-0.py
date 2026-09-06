class Solution:
    def calPoints(self, operations: List[str]) -> int:
        operators =  ['D','C','+']
        stack = []
        for c in operations:
            if c not in operators:
                stack.append(int(c))
            else:
                if c=='D':
                    stack.append(stack[-1]*2)
                if c=='C':
                    stack.pop()
                if c=='+':
                    to_add = stack[-1] + stack[-2]
                    stack.append(to_add)
        return sum(stack)

        