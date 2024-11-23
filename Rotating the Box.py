class Solution:
    def solve(self, s):
        l, r = len(s) - 1, len(s) - 1
        while l >= 0:
            if s[l] == '.':
                l -= 1
            elif s[l] == '#':
                if s[r] == '.':
                    s[l], s[r] = s[r], s[l]
                r -= 1
                l -= 1
            elif s[l] == '*':
                l -= 1
                r = l

    def rotateTheBox(self, box):
        for row in box:
            self.solve(row)
        
        m, n = len(box), len(box[0])
        ans = [[None] * m for _ in range(n)]

        for row in range(m):
            for col in range(n):
                ans[col][m - row - 1] = box[row][col]

        return ans
