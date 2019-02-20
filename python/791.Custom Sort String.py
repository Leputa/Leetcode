class Solution:
    def customSortString(self, S: 'str', T: 'str') -> 'str':
        idx2char = {}
        char2idx = {}
        for i in range(len(S)):
            idx2char[i] = S[i]
            char2idx[S[i]] = i
        T_in_S = []
        T_ = []
        for t in T:
            idx = char2idx.get(t)
            if idx != None:
                T_in_S.append(idx)
            else:
                T_.append(t)
        T_in_S = sorted(T_in_S)
        ret = []
        for idx in T_in_S:
            ret.append(idx2char[idx])
        ret += T_
        return "".join(ret)
