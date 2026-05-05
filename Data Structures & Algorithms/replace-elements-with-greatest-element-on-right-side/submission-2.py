class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_r = 0
        for i in range(len(arr)-1,-1,-1):
            item = arr[i]
            arr[i] = max_r
            if item>max_r:
                max_r = item
        arr[len(arr)-1] = -1
        return arr

        