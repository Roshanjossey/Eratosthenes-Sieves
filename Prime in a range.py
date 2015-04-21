import math
def primeinrange(rng):
  a = [True]*(rng + 1) #Make a boolean list with size range
  a[0] = a[1] = False # 0 and 1 are made composite
  # To make all even no.s except 2 composite. This decreases no. of iterations to half
  j = 4
  while j <= rng :
    a[j] = False
    j += 2
  #Now numbers from 3 to squareroot of range is checked if found as prime,all of its multiples are made composite
  i = 3
  while i <= math.sqrt(rng):
    if a[i] == True:
      j = i+i
      while j <= rng:
        a[j] = False
        j += i
    i += 2
  print('2',end=' ')
  i = 3
  while i<= rng:
    if a[i] == True:
      print(i,end = ' ')
    i += 2
  print('')
def main():
  print("Enter range:  ",end ='')
  rng = int(input())
  if rng < 2:
    print('No prime numbers')
    return(0)
  primeinrange(rng)
if __name__ == '__main__':
  main()
