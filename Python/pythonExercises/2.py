n = 17
i=0
b=0
t=0
while(n!=0):
  t=n%2
  b = b + t*(10**i)
  n=n/2
  n = int(n)
  i= i+1
print(b)