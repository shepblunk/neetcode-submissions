class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i,j = len(g)-1,len(s)-1
        g = sorted(g)
        s = sorted(s)
        count = 0
        while i>-1:
            if count==len(s):
                break
            else:
                print(s[j],g[i])
                if s[j]>=g[i]:
                    print('added')
                    count += 1
                    i-=1
                    j-=1
                elif s[j]<g[i]:
                    i-=1
        return count
                    

                



        