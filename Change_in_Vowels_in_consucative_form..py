class Solution:
    def reverseVowels(self, s: str) -> str:
        ns = s + s

        nl = []
        for i in ns:
            nl.append(i)

            

        vowel = ["a","e","i","o","u","A","E","I","O","U"]
        for i in range(len(nl)):
            if nl[i] in vowel:
            
                # print(i)
                
                for j in range(i+1,len(nl)):
                    if nl[j] in vowel:
                        print(i,j)
                        nl[i],nl[j] = nl[j],nl[i]
                        break


        ps = "".join(nl[0:len(s)])

        s = ps[:]
        return s


# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
