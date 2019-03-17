class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if hand % W != 0:
            return False