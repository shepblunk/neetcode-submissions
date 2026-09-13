class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        counter = 0
        L = 0
        hashmap = {}

        for R in range(len(s)):
            new_char = s[R]
            hashmap[new_char] = hashmap.get(new_char,0)+1

            while hashmap[new_char] >= 2:
                char_sortant = s[L]
                hashmap[char_sortant] -= 1
                if hashmap[char_sortant] == 0:
                    del hashmap[char_sortant]
                L+=1
            taille = R-L+1
            counter = max(counter,taille)
        return counter 



        """
        counter = 0
        L,R = 0,0
        hashmap = {}
        size = len(s)

        for R in range(size):
            char_entrant = s[R]
            hashmap[char_entrant] = hashmap.get(char_entrant,0) + 1

            while hashmap[char_entrant]>=2:
                # on entre dans le cas ou la fenetre n'est plus valide on décale la window
                char_sortant = s[L]
                hashmap[char_sortant] -= 1
                if hashmap[char_sortant] == 0:
                    del hashmap[char_sortant]
                L+=1

            taille = R-L + 1
            counter = max(counter,taille)
        return counter
        """            

        