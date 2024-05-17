# dict = {"china" : "143" , "indonesia":"136" , "usa":"32" , "Nepal":"34"}

# a = input("what do you want")
# k=1
# if(a=="print"):
#     print(dict)

# if(a=="add"):
#  c = input("which country do you want to add")
#  for i,v in dict.items():
#      if(i==c):
#         print("exist")
#         k=0
#         break
# if(k == 1):
#   con= input("give the country name")
#   pop = input("give the population")
#   dict[con] =pop 
#   print(dict)



# if(a=="remove"):
#   re = input("which country you want to remove")
#   for i , v , in dict.items():
#      if(i==re):
#        del dict[re]
#      else:
#         print("does not exist")

# if(a=="query"):
#    q = input("which country")
#    print(dict[q])



#2 - 

def avg(li):
    sum=0
    for i in li:
        sum=sum+i
    sum = sum/3
    sum = round(sum ,2)
    return sum  

dict = {"info":[600,630,620] , "ril":[1430,1490,1567] , "mtl":[234,180,160]}
for i , v in dict.items():
    print(f"{i}==>{v}==>avg:{avg(v)}")

st = input("stock trider")
price= input("price")
price  = int(price)
k=0
for i , v in dict.items():
    if(i==st):
        print("already exist")
        k=1
        dict[st].append(price)

if(k==0):
    dict[st] = price
    
print(dict)
