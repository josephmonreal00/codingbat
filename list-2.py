"""
Return the number of even ints in the given array. 
Note: the % "mod" operator computes the remainder, 
e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
"""
def count_evens(nums):
	count = 0
  	for i in range(0, len(nums)):
    	if nums[i] % 2 == 0:
    		count += 1
    return count

"""
Given an array length 1 or more of ints, return the 
difference between the largest and smallest values 
in the array. Note: the built-in min(v1, v2) and 
max(v1, v2) functions return the smaller or larger 
of two values.

big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
"""
def big_diff(nums):
  min_ = min(nums)
  max_ = max(nums)
  return max_ - min_


"""
Given an array of ints, return True if the array 
contains a 2 next to a 2 somewhere.

has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
"""
def has22(nums):
  	uno = 0
  	dos = 1
  	for i in range(0, len(nums) - 1):
    	if nums[i] == 2 == nums[i + 1] == 2:
      		return True
  	return False

"""
Return the "centered" average of an array of ints, 
which we'll say is the mean average of the values, 
except ignoring the largest and smallest values in the array. 
If there are multiple copies of the smallest value, 
ignore just one copy, and likewise for the largest value. 
Use int division to produce the final average. 
You may assume that the array is length 3 or more.

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
"""

def centered_average(nums):
	min_ = min(nums)
	s_ind = nums.index(min_)
	nums.remove(nums[s_ind])
  
  	max_ = max(nums)
  	l_ind = nums.index(max_)
  	nums.remove(nums[l_ind])
  
  	new_list = sorted(nums)
  
  	index_one = int(len(new_list) / 2 - 1)
  	even_index = int(len(new_list) / 2)

  	if len(new_list) % 2 == 0:
  		return int(int(new_list[index_one] + new_list[index_one + 1]) / 2)
  	else:
  		return int(new_list[even_index])