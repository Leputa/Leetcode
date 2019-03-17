from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if hand % W != 0:
            return False
        count = Counter()
        for h in hand:
            count[h] += 1
        hand = sorted(hand)
        for h in hand:
            if count[h] == 0:
                continue
            for i in range(W):
                if count[h+i] == 0:
                    return False
                count[h+i] -= 1
        return True