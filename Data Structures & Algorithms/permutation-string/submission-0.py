class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_d = [0] * 26  
        s2_d = [0] * 26  

       
        for i in range(len(s1)):
            s1_d[ord(s1[i]) - ord('a')] += 1
            s2_d[ord(s2[i]) - ord('a')] += 1

        
        matches = sum(1 for i in range(26) if s1_d[i] == s2_d[i])

        if matches == 26:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            index = ord(s2[r]) - ord('a')

            if s2_d[index] == s1_d[index]:  
                matches -= 1  
            s2_d[index] += 1
            if s2_d[index] == s1_d[index]:  
                matches += 1 
            
            index = ord(s2[l]) - ord('a')

            if s2_d[index] == s1_d[index]:  
                matches -= 1  
            s2_d[index] -= 1
            if s2_d[index] == s1_d[index]:  
                matches += 1 
            l += 1  

          
            if matches == 26:
                return True

        return False
