class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        #print(people)
        l = 0
        nb_boat = 0
        r = len(people)-1
       
        while l<=r:
            #print('while',l,r)
            if people[r] == limit:
                nb_boat += 1
                r -= 1
            else:
                sum = people[r] + people[l]
                if sum <= limit:
                    nb_boat += 1
                    l += 1
                    r -= 1
                else:
                    nb_boat +=1
                    r -= 1
           
        return nb_boat
        

        

        