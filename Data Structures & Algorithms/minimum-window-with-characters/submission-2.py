class Solution:
    def minWindow(self, s: str, t: str) -> str:
        size_s = len(s)
        size_t = len(t)
        if size_t>size_s:
            return ""

        
        hashmap_t = {}
        hashmap_window = {}

        for letter in t:
            hashmap_t[letter] = hashmap_t.get(letter,0) + 1

        #print(hashmap_t)
        need = len(hashmap_t)
        have = 0
        L = 0
        resL = 0
        resR = 0
        best = float('inf')

        for R in range(size_s):
           
            char_entrant = s[R]
            hashmap_window[char_entrant] = hashmap_window.get(char_entrant,0) + 1
            
            if hashmap_window[char_entrant] == hashmap_t.get(char_entrant,0):
                have += 1
            while have == need:
                if R-L+1<best:
                    best = R-L +1
                    resL = L
                    resR = R
                char_sortant  = s[L]

                if hashmap_window[char_sortant] == hashmap_t.get(char_sortant):
                    have -= 1

                hashmap_window[char_sortant] = hashmap_window.get(char_sortant, 0) - 1
                if hashmap_window[char_sortant] <= 0:
                    del hashmap_window[char_sortant]
                
                L+=1
            
        if best == float('inf'):
            return ""
            

        return s[resL:resR+1]


        

        
        