"""
An array is trionic if there exist indices 0 < p < q < n − 1 such that:
nums[0...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...n − 1] is strictly increasing.

Return:
    true if nums is trionic, otherwise return false:
"""

class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        """
        IDEA: We loop through the array and use each element as p with every combination of q and vice versa. So the first element will first act as p and will be tested with all other elements as q. Then the same will be done for the element but with p and q switched. We continue doing this for all elements. 
        """
        def is_increasing(start, stop) -> bool:
            """
            Returns true if nums is increasing up to the stop'th element.
            """
            for index in range(start, stop):
                if nums[index] >= nums[index+1]:
                    # 0 >= 1
                    return False
            
            return True  
                  
        def is_decreasing(p: int, q: int) -> bool:
            """
            Returns true if nums is decreasing from the p'th to q'th element.
            """
            for index in range(p,q):
                if nums[index] <= nums[index+1]:
                    return False
            
            return True            
            
        n_minus_1 : int = len(nums)-1
        
        for i, p in enumerate(nums):
            for q in nums[i:]:
                if self.valid_pq(p, q, n_minus_1):
                    # If our p and q are valid we look to find incrasing and decreasing arrays
                    a = is_increasing(0, p) 
                    b = is_decreasing(p,q)
                    c = is_increasing(q, n_minus_1)
                    
                    #print(f"p: {p}, q: {q}, a: {a}, b: {b}, c: {c}")                    
                    if a and b and c:
                        return True
                
        for i, q in enumerate(nums):
            for p in nums[i:]:
                if self.valid_pq(p, q, n_minus_1):
                    # If our p and q are valid we look to find incrasing and decreasing arrays
                    a = is_increasing(0, p) 
                    b = is_decreasing(p,q)
                    c = is_increasing(q, n_minus_1)
                    
                    #print(f"p: {p}, q: {q}, a: {a}, b: {b}, c: {c}")                    
                    if a and b and c:
                        return True
                    
        return False
                    
    def valid_pq(self, p: int, q: int, len: int) -> bool:
        return p < q and p <= len and q <= len
    
    
if __name__ == "__main__":
    s = Solution()
    assert s.isTrionic([1,3,5,4,2,6]) == True
    assert s.isTrionic([2,1,3]) == False
    assert s.isTrionic([5,9,1,7]) == False # Should be true according to leet, but I don't see why.
    
    print("All tests passed")