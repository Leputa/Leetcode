class Solution:
    def deckRevealedIncreasing(self, deck: 'List[int]') -> 'List[int]':
        deck = sorted(deck)
        length = len(deck)
        queue = list(range(length))
        cnt = 0
        cmap = [0] * length
        while len(queue) != 0:
            cnt += 1
            t = queue.pop(0)
            if cnt % 2 == 1:
                cmap[t] = deck.pop(0)
            else:
                queue.append(t)
        return [cmap[i] for i in range(length)]
