import random
a = [1,2,3,4,5,6,7,8,9]
i = 0
high = 0
low = 0
exact = 0
total_guess = 0
while True:
   user_input = input("Guess a number between 1 and 9 ")
   if user_input == "exit": break
   user_input = int(user_input)
   i = random.randint(1,9)
   print("Random Number = %d" %i)
   if user_input > i: 
      print("Your guess too high"); high += 1
   if user_input < i: 
      print("Your guess too low"); low += 1
   if user_input == i: 
      print("Congratulation! you guess it correctly"); exact += 1
total_guess = high + low + exact
print ("Your total guess = %d" %total_guess)
print ("Guess High = %d; Guess Low = %d; Guess Exact = %d" %(high, low, exact))

   
   
   
