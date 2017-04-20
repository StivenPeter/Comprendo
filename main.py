def minThresh(s):
  u = len([letter for letter in s if letter.isupper()])
  l = len([letter for letter in s if letter.islower()])
  n = len([letter for letter in s if letter.isdigit()])
  if u > 0 and l > 0 and n > 0: 
    return True 
  return False 
  
