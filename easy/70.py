class Solution:
    """
    Use bruteforce to recurse through the nums. However this will exceed time limits, so we store previously 
    calculated values in an array and re-use instead of re-calculating.
    This is a fibonacci series and can be easily solved with the fibonacci function.
    """
    nums_list: list[int] = [-1 for i in range(46)]
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1 
        elif n == 2:
            return 2
        elif self.nums_list[n] != -1:
            return self.nums_list[n]
        self.nums_list[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.nums_list[n]


            


s = Solution()
print(s.climbStairs(44))
