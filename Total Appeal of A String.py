class Solution:
    def appealSum(self, s: str) -> int:
        cur, res, book = 0, 0, defaultdict(lambda:-1)
        for i, ch in enumerate(s):
            cur += i - book[ch]
            res += cur
            book[ch] = i
        return res
 #NOT BAD FOR A HARD
