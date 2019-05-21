class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        alphabet = list(map(chr, range(ord("a"), ord("z") + 1)))
        idx = 0
        ret = []
        while(idx < len(alphabet)):
            alpha = alphabet[idx]
            is_choose = True
            for a in A:
                if alpha not in a:
                    is_choose = False
                    break
            if is_choose == False:
                idx += 1
            else:
                ret.append(alpha)
                for i in range(A):
                    A[i].remove(alpha)
        return ret

