class Solution:
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

s = Solution()
print(s.removeElement([5,2,5,2,1,6,2,6,3,4,1,2,6,6],2))

