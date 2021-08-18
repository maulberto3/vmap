nums = [1,2,3,4,5,6,7,8,9]

print('''How to compute the standard
deviation from scratch?''')

mean = sum(nums) / len(nums)

std = [x-mean for x in nums]
std = [x**2 for x in std]
std = sum(std)
std /= (len(nums)-1)
std = std**0.5

print(std)

from statistics import stdev
print(stdev(nums))
