import random
print("Welcome to Number Guessing Game!")
print("You have to guess a number between 1 and 100.")
sn = random.randint(1, 100)
attempt = 0 
while True:
      print("Enter your guess:")
      print("are you want to quit (y/n)?")
      c = input().lower()
      if c == 'y':
          print("Thank you for playing!")
          break
      if not gn.isdigit():
            print("Please enter a valid number.")
            continue 
      attempt += 1  
      gn = int(gn)     
      if sn == gn:
            print("Congratulations! You guessed the correct number.")
            break
      elif  sn < gn:
            print("Your guess is too low. Try again.")
      else:
            print("Your guess is too high. Try again.")

      
print("codmetric")
