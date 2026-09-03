import math


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Loop through each string concurrently and build the LCP as we go.
        """
        def len_of_shortest_str_in(strs) -> int:
                shortest_yet : int = math.inf
                for str in strs:
                    length = len(str)
                    if length < shortest_yet:
                        shortest_yet = length
                return shortest_yet
            
        res = ""
        
        range_loop = len_of_shortest_str_in(strs)
        
        for i in range(range_loop):
            prefix = ""
            first = True
            for str in strs:
                if first:
                    char = str[i]
                    prefix += char
                    res += char
                    first = False
                else:
                    if str[i] != prefix[-1]:
                        res = res[:-1]
                        return res
                
        return res
                    