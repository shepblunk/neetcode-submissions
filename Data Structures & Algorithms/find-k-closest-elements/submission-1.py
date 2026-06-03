import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        tas = []
        res = []
        for e in arr:
            heapq.heappush(tas,(abs(x-e),e))

        #print(tas)

        for i in range(k):
            little = heapq.heappop(tas)
            #print('little',little)
            valeur = little[1]
            res.append(valeur)

        #print(res)
        res.sort()

        return res
        