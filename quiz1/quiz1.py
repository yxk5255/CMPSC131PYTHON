def f1(n):
n = int(input("Enterryour number : "))
if n<0 :
    n = n*-1
print(n) 

def f2(n):
sum = 0
f = int(input("How many times should I add? -->"))
for i in range(f):
    n = int(input("What is your number> -->"))
    if n<0:
        n = n*-1
    sum = sum + n
print(sum)
  
def run():
  n = int(input("What is your number? -->"))
  print(f2(n))
  return

if True: 
  run()
