class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)==1:
            return False

        hashmap = {
            123 : 125,
            91 : 93,
            40 : 41
        }    

        stack=[]

        for i in range(len(s)):
            x = ord(s[i])
            
            if x in hashmap:
                stack.append(x)

            else:
                print('current' , x)
                if stack:
                    last_element = stack.pop()
                    
                    if x != hashmap[last_element]:
                        return False
                else:
                    return False

    
        return len(stack)==0
