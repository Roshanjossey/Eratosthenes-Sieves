import math
def erat(rng):
  a = [i for i in range(rng)]# Here we are using integer list so that we can store biggest prime factors of all numbers this will come handy in prime factorization
  j = 4
  while j < rng:
    a[j] = 2
    j += 2
  i = 3
  while i < math.sqrt(rng):
    if a[i] == i:
      j = i+i
      while j < rng:
        a[j] = i
        j += i
    i += 2
  def primfac(c):
    if a[c] == c:
      print(c)
    else:
      print(a[c],' * ',end='')
      primfac(int(c/a[c]))
  i = 1
  while i != 0:
    print('Enter number to prime factorize 0 to exit : ')
    i = int(input())
    if i > rng:
      print('Out of range')
      continue
    primfac(i)
def main():
  print('Enter Range: ')
  rng = int(input())
  erat(rng)
if __name__ == '__main__':
  main()
