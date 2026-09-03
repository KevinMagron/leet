class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        We iterate through the stringified int from the beginning and back and make sure that they match. If they don't match it must be the middle number and we return True.
        """
        if x < 0:
            return False

        stringified_x : str = str(x)
        middle : int = self.middle_number(stringified_x)
        middle_int : int = self.middle_index(stringified_x)

        for i,num in enumerate(stringified_x):
            if stringified_x[-i-1] != num and i != middle_int:
                return False
            if i+1>middle_int:
                return True


    def middle_number(self, p: str) -> str:
        if len(p)%2 == 0:
            return ""
        return p[len(p)//2]

    def middle_index(self, p: str) -> int:
        return len(p)//2


