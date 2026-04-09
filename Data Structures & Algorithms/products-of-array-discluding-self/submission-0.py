class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def gauche(nums):
            res = []
            sous_tot = 1
            for j in range(0,len(nums)):
                ###print("j",j)
                res.append(sous_tot)
                ###print("on ajoute",sous_tot)
                sous_tot *= nums[j]
               
            return res

        def droite(nums):
            res = [0]*len(nums)
            sous_tot = 1
            for j in range(len(nums)-1,-1,-1):
                res[j]= sous_tot
                sous_tot *= nums[j]
                ####print("sous total",sous_tot)
            return res

        ###print(gauche(nums),droite(nums))
        res = [x*y for x,y in zip(droite(nums),gauche(nums))]
        ####print(res)
        return res
        