class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        if len(sequence) == 1:
            return True
        return self.splitTree(sequence)
        
    def splitTree(self, sequence):
        if len(sequence)<=1 :
            return True
        root = sequence[len(sequence)-1]

        split = -1
        for i in range(len(sequence)):
            if sequence[i] > root:
                split = i
                break
        if split == -1:
            split = len(sequence)-1

        for i in range(split,len(sequence)):
            if sequence[i] < root:
                return False

        return self.splitTree(sequence[:split]) and self.splitTree(sequence[split:len(sequence)-1])


print(Solution().VerifySquenceOfBST([4,8,6,12,16,14,10]))
