class Solution:
    def commonChars(self, s):
        l = []
        # iterate over the first string
        for c in range(len(s[0])):
            # initially common is true
            Common = True
            # then iterate and check for other strings 1 to last
            for j in range(1, len(s)):
                # if any char of s[0] not in other string then common is false
                if s[0][c] not in s[j]:
                    Common = False
                    break
            # if any char of s[0] present in other strings then common is true
            if Common:
                # add it to common list
                l.append(s[0][c])
                # remove the char from other strings that is matched and added in common list
                for word in range(1, len(s)):
                    # index of the char that is matched among all strings 
                    i = s[word].index(s[0][c])
                    s[word] = s[word][:i] + s[word][i + 1:]
        return l

# Example usage:
s = ["bella", "label", "roller"]
solution = Solution()
result = solution.commonChars(s)
print(result)

            
            
    