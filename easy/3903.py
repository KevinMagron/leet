class Solution:
    """
    We loop through the list and caclulate the insatbility score. If it's stable and the lowest so far, save the index
    otherwise continue. Return the smallest index : -1
    """
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            roof: int = max(nums[:i+1])
            floor: int = min(nums[i:])
            score: int = roof-floor
            if score <= k:
                return i

        return -1

             
    def firstStableIndexImproved(self, nums: list[int], k: int) -> int:
        current_max = 0
        current_min = min(nums)
        len_nums = len(nums)

        for i in range(len_nums):
            if nums[i]>current_max:
                current_max=nums[i]

            score = current_max-current_min

            if score <= k:
                return i

            if nums[i] == current_min and i!=len_nums-1:
                current_min = min(nums[i+1:])

        return -1


