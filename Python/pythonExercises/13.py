f = open("road.txt" , "r")
t = {}
i = 0

for x in f:
   a = f.readline()
   arr = a.split(" ")
   for y in arr:
      k=0
      for z,b in t.items():
         if(z==y):
            t[y] = t[y]+1
            k = 1
            break

      if(k==0):
        t[y] = 1

print(t)        