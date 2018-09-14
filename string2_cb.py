"""
Given a string, return a string where for every char in the original, 
there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
"""
def double_char(str):
	newStr = ""
  	for i in range(0, len(str)):
    	newStr += str[i] * 2
  	return 

"""
Return the number of times that the string "hi" appears anywhere in 
the given string.


count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""
def count_hi(str):
  count_ = str.count("hi")
  return count_

"""
Return True if the string "cat" and "dog" appear the same number of times 
in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""
def cat_dog(str):
  	dog_ = str.count("dog")
  	cat_ = str.count("cat")
  	if dog_ == cat_:
    	return True
  	else:
    	return False

"""
Return the number of times that the string "code" appears anywhere in the 
given string, except we'll accept any letter for the 'd', so "cope" and 
"cooe" count.


count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""
def count_code(str):
  	c_ = 0 
  	o_ = 1
  	e_ = 3
  	count = 0
  	lower_ = str.lower()
  	for i in range(0, len(lower_) - 3):
    	if lower_[c_] == "c" and lower_[o_] == "o" and lower_[e_] == "e":
      		count += 1
    	c_ += 1
    	o_ += 1
   	 	e_ += 1
  	return count

"""
Given two strings, return True if either of the strings appears at the 
very end of the other string, ignoring upper/lower case differences 
(in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
"""
def end_other(a, b):
  	a_lower = a.lower()
  	b_lower = b.lower()
  	a_len = len(a_lower) 
  	b_len = len(b_lower)
  	if a_len < b_len:
    	#if a_lower[-(a_len): len(a)] == b[-(a_len): len(b)]:
    	if a_lower[0: len(a)] == b_lower[-(a_len): len(b)]:
      		return True
    	else:
      		return False
  
  	if b_len < a_len:
    	#if b_lower[-(b_len): len(b)] == a[-(b_len): len(b)]:
    	if b_lower[0: len(b)] == a_lower[-(b_len): len(a)]:
      		return True
    	return False

"""
Return True if the given string contains an appearance of 
"xyz" where the xyz is not directly preceeded by a period 
(.). So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
"""
def xyz_there(str):
  	add = 3

  	if len(str) <= 2 or "xyz" not in str:
    	return False
    
	"""
	Starting for loop at index 1 and checking whether or not
	first element at index 0 is a . or not
	  
	.xyzasd
	0123456 = 7
	    E
	range(1, len(str) - 3) 
	"""
 	first_ind = str[0] 
  	
  	last_x = ""
  	for i in range(0, len(str)):
    	if str[i] == "x":
      		last_x = i
      
  	if first_ind == "." and len(str) <= 4:
    	return False
    
  	for i in range(0, len(str) - 3):
    	if first_ind == "." or str[last_x - 1] == ".":
      		return False
  	return True

