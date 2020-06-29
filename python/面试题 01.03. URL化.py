class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:    
        if len(S) > length:
            S = S[:length]
        else:
            S += " " * (length - len(S))
        return S.replace(" ", "%20")