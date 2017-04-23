
def lengthofs(s):
  u = len([letter for letter in s if letter.isupper()])
  l = len([letter for letter in s if letter.islower()])
  n = len([letter for letter in s if letter.isdigit()])
  aln = len([letter for letter in s if letter.isalnum()])
  return [u,l,n,aln]

def isminThresh(s):
  res = lengthofs(s)
  if res[0] > 0 and res[1] > 0 and res[2] > 0: 
    return True 
  return False 
  
def minrating(s):
  if isminThresh(s) == False:
    return 1
  ret = 1
  res = lengthofs(s)
  if res[0]>3:
    ret+=3
  else:
    ret+=res[0]
  if res[1]>3:
    ret+=3
  else:
    ret+=res[1]
  if res[2]>3:
    ret+=3
  else:
    ret+=res[2]
  return ret
#print "password strength"+"(GOOdni647): "+str(minrating("GOOdni647"))
