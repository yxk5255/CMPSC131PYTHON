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
  """
  This function returns True if s is a palindrome, i.e.,
  if s reads the same backward as forward, returns False otherwise.
  You must implement this with a while loop that compares
  characters in s one by one going forward vs. going backward
  """

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
  """
  This function returns True if s is a palindrome, i.e.,
  if s reads the same backward as forward, returns False otherwise.
  You must implement this function with recursion. A string is a
  palindrome only if its first character and its last
  character are the same AND the middle (smaller) part is a palindrome.
  Use negative index to get the last character and use
  slicing to get the middle of the string.
  """
s = input(("Enter a string:"))
if(s==s[::-1]):
      return True
else:
      print("Not a palindrome")
      return False

def is_palindrome3(s):
  """
  This function returns True if s is a palindrome, i.e.,
  if s reads the same backward as forward, returns False otherwise.
  You must implement this function with a one-liner.
  Use slicing (with step being -1) to get the reverse of a
  string, and a string is a palindrome if it is equivalent to its reverse.
  """
  return True

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

