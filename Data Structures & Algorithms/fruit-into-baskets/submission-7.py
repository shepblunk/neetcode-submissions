class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        L = 0
        best = 0
        hashmap = {}

        for R in range(len(fruits)):
            fruit_droite = fruits[R]
            hashmap[fruit_droite] = hashmap.get(fruit_droite,0) + 1

            while len(hashmap)>2:
                fruit_gauche = fruits[L]
                hashmap[fruit_gauche] -= 1
                if hashmap[fruit_gauche] == 0:
                    del hashmap[fruit_gauche]
                L += 1

            best = max(best,R-L+1)
                
        return best




        