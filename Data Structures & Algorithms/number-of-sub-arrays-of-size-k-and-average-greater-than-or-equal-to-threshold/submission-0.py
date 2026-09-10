class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        count = 0
        average = 0
        nb = 0

        for r in range(len(arr)):
            average_courant = sum(arr[left:r+1]) / len(arr[left:r+1])
            #print(average_courant)
            size = r-left+1
            if size==k:
                if average_courant>=threshold:
                    count += 1
                left += 1
            

        return count
                
        