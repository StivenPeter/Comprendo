
def lengthofs(s):
  u = len([letter for letter in s if letter.isupper()])
  l = len([letter for letter in s if letter.islower()])
  n = len([letter for letter in s if letter.isdigit()])
  aln = len([letter for letter in s if letter.isalnum()])
  return [u,l,n,an]

def isminThresh(s):
  res = lengthofs(s)
  if res[0] > 0 and res[1] > 0 and res[2] > 0: 
    return True 
  return False 
  
def minrating(s):
  if isminThresh(s) == False:
    return 1
  res = lengthofs(s) 
