class Solution:
    """ Think of the array as a graph, then recursively solve every of its neighbours. """ 
    def canJumpRec(self, nums: list[int]) -> bool: 
        if len(nums) == 1: 
            return True 
        elem = nums[0]
        for i in range(elem): 
            res = self.canJump(nums[i+1:]) 
            if res: return True 

        return False
    
    """
    Iterate through since recursive solution requires to much memory, from slicing the array
    """

    def canJumpIter(self, nums: list[int]) -> bool:
        for i in range(nums):
            res = self.canReach(nums[i], nums)

    def canReach(self, pos, nums):
      
        if pos == len(nums)-1: 
            return True

        

a = [0,2,3]
b = [2,5,7,2]
s = Solution()
print(s.canJump(a))
