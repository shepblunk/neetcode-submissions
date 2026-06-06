class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False


        window_size = len(s1)

        hashmap_s1={}
        hashmap_window = {}
        for i in range(window_size):
            char1 = s1[i]
            char2 = s2[i]
            hashmap_s1[char1] = hashmap_s1.get(char1,0) + 1
            hashmap_window[char2] = hashmap_window.get(char2,0) + 1
            

        if hashmap_window == hashmap_s1:
                return True
        
        L = 0
        R = len(s1)

        
        while R < len(s2):
            char_entrant = s2[R]
            char_sortant = s2[L]

            hashmap_window[char_entrant] = hashmap_window.get(char_entrant, 0) + 1
            hashmap_window[char_sortant] -= 1
            
            # 4. On SUPPRIME la clé UNIQUEMENT si son compteur atteint 0
            if hashmap_window[char_sortant] == 0:
                del hashmap_window[char_sortant]

            # 5. On compare les dictionnaires
            if hashmap_window == hashmap_s1:
                return True
                
            # 6. On fait avancer la fenêtre
            L += 1
            R += 1
            
        
        return False
        