def f1(a):
k = int(input("Enterryour number : "))
if k<0 :
    k = k*-1
print(k) 

def f2(n):
sum = 0
f = int(input("How many times should I add? -->"))
for i in range(f):
    x = int(input("What is your number> -->"))
    if x<0:
        x = x*-1
    sum = sum + x
print(sum)
  
def run():
  n = int(input("What is your number? -->"))
  print(f2(n))
  return

if True: 
  run()
