import random
n = random.randint(1,100)
max_attempts = 7
attempts = 0
print("GUESS THE NUMBER BETWEEN 1 AND 100!")
while attempts < max_attempts:
    try:
        num = int(input("Enter guess: "))
        attempts += 1
        if num <= 0:
           print("NUMBER MUST BE GREATER THAN ZERO!")
        elif num == n:
           print(f"CORRECT! YOU HAVE GUESSED IT IN {attempts} ATTEMPTS")
           break
        elif num < n:
           print("TOO LOW! TRY AGAIN...")
        else:
            print("TOO HIGH! TRY AGAIN...") 
        print(f"ATTEMPTS LEFT: {max_attempts - attempts}")    
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER!") 
else:
    print("GAME OVER!")  
    print(f"THE CORRECT NUMBER WAS {n}")                        
