# Author: Yanling Wang yuw17@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 1
# Breakout: 1

# Author: Yanling Wang yuw17@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 1
# Breakout: 1

def is_palindrome1(s):
  s = input("Enter the string: ")
  k = s
  rev = ""
    while(len(k) > 0):
      if(len(k) > 0):
        a = k[-1]
        k = k[:-1]
      rev = rev + a
  if(rev == s):
    return True
  else:
    return False
  
def is_palindrome2(s):
  s = input(("Enter a string:"))
  if(s==s[::-1]):
      return True
  else:
      print("Not a palindrome")
      return False
    
def is_palindrome3(s):
  s = input("Enter the string: ")
  if str(s) == str(s)[::-1]:
    return True
  else:
    return False
  
def run():
  s = input("Enter a string: ")
  print(is_palindrome1(s))
  print(is_palindrome2(s))
  print(is_palindrome3(s))

  if __name__ == "__main__":
    run()

