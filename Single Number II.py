def singleNumber(self, nums: List[int]) -> int:
	num = list(set(nums))
	for i in num:
		if nums.count(i) == 1:
			return i
  #Simple solution yet it works, no optimization was asked in the problem.
