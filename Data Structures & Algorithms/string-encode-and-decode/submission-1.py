from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            # On stocke la longueur du mot + '#' + le mot lui-même
            res += str(len(string)) + "#" + string
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # On cherche où se trouve le séparateur '#'
            while s[j] != '#':
                j += 1
            
            # On extrait la longueur du mot
            length = int(s[i:j])
            
            # On extrait le mot exact grâce à sa longueur
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # On avance l'indice après le mot extrait
            i = j + 1 + length
            
        return res

# Exemple d'utilisation :
prout = Solution()
encoded = prout.encode(["apagnan", "prout#avec#hash"])
print("Encodé :", encoded)  # Résultat : "7#apagnan15#prout#avec#hash"

decoded = prout.decode(encoded)
print("Décodé :", decoded)  # Résultat : ['apagnan', 'prout#avec#hash']