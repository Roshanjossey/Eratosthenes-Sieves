def primeinrange(rng):
  a = [True]*(rng + 1) #Make a boolean list with size range
  a[0] = a[1] = False # 0 and 1 are made composite
  # To make all even no.s except 2 composite. This decreases no. of iterations to half
  j = 4
  while j < rng :
    a[j] = False
    j += 2
  #Now numbers from 3 to spuareroot of range is checked if found as prime,all of its multiples are made composite
  i = 3
  while i < math.sqrt(rng):
      if a[i] == False:
      j = i+i
      while j < 2000001:
        a[j] = i
        j += i
  i += 2
#print(a)
def primsum(c):
  if a[c] == c:
    return(c)
  else:
    return(a[c]+primsum(int(c/a[c])))
tots = 0
for x in range(int(input())):
  n = int(input())
  tots += primsum(n)
print(int(tots))
