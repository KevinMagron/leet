class Solution:
    """
    This solution is brute-forced and manipultes an index.
    """
    def removeElement(self, nums: list[int], val: int) -> int:
        def elem_in_nums(index: int) -> bool:
            return nums[index] == val 

        n: int = len(nums)
        i: int = 0

        while i < n:
            if elem_in_nums(i):
                nums.pop(i)
                n-=1
            else:
                i+=1

        return n

    """
    The second solution utilizes 2 different indexes, one for reading and one for writing. It solves it exactly according to the constraints, not more or less. Adding a del[w_p:] would also remove any remaining tail.
    """
    def removeElementPointers(self, nums: list[int], val: int) -> int:
        r_p: int = 0 # read pointer for reading every val of nums
        w_p: int = 0 # pointer to write accepted values to nums

        for r_p in range(len(nums)):
            current_val = nums[r_p]
            if current_val != val:
                nums[w_p] = current_val
                w_p+=1
                final_len+=1
        
        return w_p

s = Solution()
print(s.removeElement([5,2,5,2,1,6,2,6,3,4,1,2,6,6],2))

"""
Overall I'd prefer the second solution for readability and performance since pop() is not used and its more difficult to follow the index than having 2 different. The second also reminds me of a turing machine which is cool.
"""
