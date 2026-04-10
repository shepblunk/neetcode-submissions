class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0] * len(temperatures)
        stack = []
        size = len(temperatures)

        for i in range (size): 
            # print('on traite' , temperatures[i])
            
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            
            stack.append(i)
                            
        return res