class Solution:
    """
    Find the min and max value in nums and remove them. Removal is done by removing from the front or back of the
    array. Return the minimum number of removals.
        
    IDEA: loop through nums and compare each val with the so far min and max values. When looped through, see if its
    best to remove from front or back. Then return the minimal number of removals.
    """
    def minimumDeletions(self, nums: list[int]) -> int:
        nums_len: int = len(nums)

        def remove_from_front(i: int) -> bool:
            return i <= nums_len // 2

        min: int = null 
        min_index: int = 0 
        max: int = null 
        max_index: int = 0
       
        for i in range(len(nums)):
            current_val = nums[i]
            if i == 0:
                min, max = current_val # first val 
            elif current_val < min:
               min = current_val 
               min_index = i
            elif current_val > max:
                max = current_val
                max_index = i
        
        min_remove: int = 0

        # case 1: both from front
        if self.remove_from_front(min_index+1) and self.remove_from_front(max_index+1):
            min_remove = max(min_index+1,max_index+1)
        # case 2: min front and max back

        # case 3: min back and max front

        # case 4: both from back

# [1,3,2,10,2,6]
# min = 1, min_index = 1
# max = 10, max_index = 4
# len = 6 => 6//2 = 3 => 
# min_i <= 3, max_i !<= 3
# count = +min_index 
# count+= 
