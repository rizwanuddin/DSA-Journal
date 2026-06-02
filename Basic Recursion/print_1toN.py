class Solution:
    def printNumbers(self, N, current):
        if current > N:
            return
        print(current, end=" ")
        self.printNumbers(N, current+1)
if __name__== "__main__":
    sol = Solution()
    N = 4
    sol.printNumbers(N, 1)
