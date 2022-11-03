import random

user_min = int(input("Please enter a three digit number:"))
user_max = int(input("Please enter a three digit number higher than your previous number: "))

#Make sure min and max are >= 50 apart:
if user_max < user_min + 50:
    print("Please enter a higher number.")
    user_max = int(input())

password = random.randint(user_min,user_max)
print("(the password is", password,")!TAKE THIS OUT LATER!")
print("The password is a number between ", user_min, " and ", user_max)

#Hint 1: password is divisible by:
if password%2 == 0:
    print("The password is divisible by 2.")
elif password%3 == 0:
    print("The password is divisible by 3.")
elif password%5 ==0:
    print("The password is divisible by 5.")
elif password%7 == 0:
    print("The password is divisible by 7.")


#Hint 2: sum of digits:
pass_list = [str(password)[i:i+1] for i in range(0, len(str(password)), 1)]
pass_sum = 0
for num in pass_list:
    pass_sum+= int(num)
print("The sum of the digits of the password is",pass_sum )

if int(pass_list[0]) < 5:
    print("The first digit is less than 5.")
else:
    print("The first digit is greater than or equal to five.")

print("Please enter a guess: ")


def password_guesser(idx):
    user_guess = input()
    user_guess_list = [user_guess[i:i+1] for i in range(0, len(user_guess), 1)]
    print(user_guess_list)
    while user_guess_list[idx] != int(pass_list[idx]): 
            if user_guess == password:
                print("Access granted.")
                break
            for i, num in enumerate(user_guess_list):
                if user_guess_list[i] == int(pass_list[idx]):
                    print("For digit ", int(idx)+1)
                    print("Your digit is correct.")
                elif user_guess_list[i] != int(pass_list[idx]) and user_guess_list[i] != 0:
                    print("For digit", int(idx)+1)
                    print("Your digit is", int(num)/int(pass_list[idx]), "times larger than the actual digit. Guess again:")
                    user_guess = input()
                elif int(pass_list[idx]) == 0:
                    print("For digit ", int(idx)+1)
                    print("Your digit is", pass_list[idx], "larger than the actual digit.")
                    user_guess = input()



password_guesser(0)

if pass_list[1]%2 == 0:
    print("The second digit is even.")
else:
    print("The second digit is odd.")

password_guesser(1)

if pass_list[2]%2 == 0:
    print("The third digit is even.")
else:
    print("The third digit is odd.")




