# 27 Feb 2024

def havefun(n):
  if n == 0:
    return 0
  else:
    print("output = ", n)
return havefun(n-1)

havefun(10)

def nontail(x):
  if(x == 0):
    return 0
  nontail(x-1)
  print("output = ", x)

nontail(10)
  
