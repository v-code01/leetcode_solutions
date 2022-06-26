class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        def f(a):
            last = {}
            for i, v in enumerate(a):
                if v in last:
                    yield i - last[v] + 1
                last[v] = i

        return min(f(cards), default=-1)
     #IM BACK

        
