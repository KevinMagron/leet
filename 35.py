class Solution:
      def searchInsert(self, nums: list[int], target: int) -> int:
        """
        Given array nums with sorted integers, if the target is in it the index of it in the list shall be returned, otherwise the index which the target would've had shall be returned

        IDEA: Since constraint is logn complexity we cant loop from start to finish, we do binary search and use the length as index. We'll eventually find our target and know the index simultaneously.
        """  
        left : int = 0
        right : int = len(nums) - 1
        

        while left <= right:
            middle = ( left + right ) // 2
            val = nums[middle]
            if val == target:
                return middle
            elif val < target:
                left=middle+1 
            else:
                right=middle-1
        return left 


arr = [1,3,5,6]
# left = 0, right = 3, middle = 1
# a[1] = 3 > 2 => right = 2
# left = 0, right 2, middle = 1
# a[1] 0 3 > 2 => 

s = Solution()
print(s.searchInsert(arr, 2))

