class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        #print(nums)
        cmin = 0
        cmax = max(nums) - min(nums)

        while cmin<cmax:
            cmid = (cmin+cmax)//2
            #print(cmid,'cmid')
            count = 0
            i=0
            while i<len(nums)-1:
                z = abs(nums[i]-nums[i+1])
                if z<=cmid:
                    count +=1
                    i+=2
                else:
                    i+=1
    

            #print('count',count)
            if count>=p:
                cmax = cmid
            else:
                cmin = cmid+1

            #print(cmin,cmax)

             
        return cmin
        