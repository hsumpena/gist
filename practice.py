a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
y = " "
print("Please, enter a number")
num = int(input())
for x in a:
  if x < num : y += str(x) + " "
print(y)
