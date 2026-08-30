class Solution: 
    """
    Given a haystack word, look for the first occurence of the needle in it and return the index of where it starts
    
    IDEA: Loop through haystack and search for firstLetter of needle. If found, send the entire len(needle) coming after the found letter in haystack, to helper function. If it matches, return True, otherwise continue the loop.
    """
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len: int = len(needle)

        def matches_needle(start: int) -> bool:
            end: int = start + needle_len
            for j in range(start:end):
                if haystack[j] != needle[j-start]:
                    return False 
            return True 

        first_letter: str = needle[0]
        
        for i in range(len(haystack)-needle_len+1):
            if haystack[i] == first_letter:
                match : bool = matches_needle(i)
                if match:
                    return i 
        return -1

s = Solution()
print(s.strStr("sadbutsad", "sad"))
