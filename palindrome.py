a = input ("Enter a string ")
i = len(a)-1
b =""
while i >= 0:
  b = b + a[i]
  i -= 1
print(a)
print(b)
if a == b : print("It is Palindrome")
else: print("It is NOT Palindrome")