from collections import Counter as C
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return C(s) == C(t)   # Counter is a container that will hold the count of each of                                 
                              # the elements present in the container.