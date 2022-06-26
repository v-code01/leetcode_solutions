#BRUTE FORCE ACCEPTED :)
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        res = set()
    
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                res.add(tuple(nums[i:j]))

        ans = [i for i in res if sum([j%p == 0 for j in i]) <= k]

        return len(ans)
      
# I DECIDED TO TRY TO OPTIMIZE IT FOR FUN ANYWAYS
class Solution:
    def countDistinct(self, a: List[int], k: int, p: int) -> int:
        t = {}
        
        n = len(a)
        res = 0
        for i in range(n):
            node = t
            count = 0
            for j in range(i, n):
                count += int(a[j] % p == 0)
                if count <= k:
                    res += a[j] not in node
                    node = node.setdefault(a[j], {})
                else:
                    break
        return res
