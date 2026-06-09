class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        size = len(s)
        hashmap = {}
        best = 0

        for R in range(size):
            char_entrant = s[R]
            hashmap[char_entrant] = hashmap.get(char_entrant,0) + 1
            max_freq = max(hashmap.values())
            if R-L+1-max_freq<=k:
                best = max(best , R-L +1)
            else:
                char_sortant = s[L]
                hashmap[char_sortant] -= 1
                if hashmap[char_sortant] == 0:
                    del hashmap[char_sortant]
                L+=1
        return best
            

            #R - L + 1 - max_freq <= k
        