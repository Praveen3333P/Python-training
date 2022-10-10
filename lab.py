import re 
 
st = input("Enter string: ") 
substring = input("Enter substring: ") 
 
pattern = "^" + substring 
if re.match(pattern, st): 
    print("Substring is the start of the string.") 
else: 
    print("Substring is not the start of the string.") 
