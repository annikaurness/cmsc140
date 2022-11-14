import random


print("Welcome to password guesser.")
user_min = input("Please enter a three digit number:")
if user_min.isdigit() == False:
    print("That doesn't look like a number. Please try again.")
    user_min = input("Please enter a three digit number:")
user_max = input("Please enter a three digit number higher than your previous number: ")
if user_max.isdigit() == False:
    print("That doesn't look like a number. Please try again.")
    user_max = input("Please enter a three digit number higher than your previous number: ")

#Make sure min and max are >= 50 apart:
if int(user_max) < int(user_min) + 50:
    print("Please enter a higher number.")
    user_max = input()
    if user_max.isdigit() == False:
        print("That doesn't look like a number. Please try again.")
        user_max = int(input())

password = random.randint(int(user_min),int(user_max))
# print("(the password is", password,")!TAKE THIS OUT LATER!")
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
user_guess = input()
if user_guess.isdigit() == False:
    print("That doesn't look like a number. Please try again.")
    user_guess = input()
guess_counter = 5 
while user_guess != password: 
    user_list = [str(user_guess)[i:i+1] for i in range(0, len(str(user_guess)), 1)]
    if int(user_guess) == password:
        print("Access granted.")
        break
    if guess_counter == 0:
        print("Sorry, you're out of guesses.")
        break
    elif int(user_guess) <= password+25 and int(user_guess) >= password-25:
            print("Good guess.Your number is less than 25 greater or less than the password. But the real password's second digit is",int(pass_list[1])-int(user_list[1]), "more than the second digit in your guess.")
            guess_counter-=1
            print("Guesses left: ", guess_counter)
    else:
            print("Not a bad guess. But the real password is at least 25 less or more, and the real second digit is", int(pass_list[1])-int(user_list[1]), "more than the second digit in your guess.")
            guess_counter-=1
            print("Guesses left: ", guess_counter)

    user_guess = input("Guess again: ")
    if user_guess.isdigit() == False:
        print("Please enter a number.")

    if int(user_guess) == password:
        print("Access granted.")
        break
    if guess_counter == 0:
        print("I'm sorry, you're out of guesses.")
        break
    elif int(user_guess[0]) == int(user_guess[1]) or int(user_guess[1]) == int(user_guess[2]) or int(user_guess[0]) == int(user_guess[2]) and pass_list[0]!= pass_list[1] and pass_list[1]!= pass_list[2] and pass_list[0]!= pass_list[2]: #error here
        print("Close, but the real password doesn't have any repeated digits.")
        guess_counter-=1
        print("Guesses left: ", guess_counter)
        if guess_counter ==0:
            print("Sorry, you're out of guesses.")
            break
    elif int(user_guess[0]) == int(user_guess[1]) or int(user_guess[1]) == int(user_guess[2]) or int(user_guess[0]) == int(user_guess[2]) and pass_list[0]== pass_list[1] or pass_list[1]== pass_list[2] or pass_list[0] == pass_list[2]:
        print("Close, at least two of the real password's digits are the same.")
        guess_counter-=1
        print("Guesses left: ", guess_counter)
        if guess_counter ==0:
            print("Sorry, you're out of guesses.")
            break
    elif int(user_guess[0]) != int(user_guess[1]) and int(user_guess[1]) != int(user_guess[2]) and int(user_guess[0]) != int(user_guess[2]) and pass_list[0]== pass_list[1] or pass_list[1]== pass_list[2] or pass_list[0] == pass_list[2]:
        print("Close, but the real password has at least two digits that are the same.")
        guess_counter-=1
        print("Guesses left: ", guess_counter)
        if guess_counter ==0:
            print("Sorry, you're out of guesses.")
            break
    else:
        print("Close, all of the real password's digits are unique.")
        guess_counter-=1
        print("Guesses left: ", guess_counter)
        if guess_counter ==0:
            print("Sorry, you're out of guesses.")
            break

    user_guess = input("Guess again: ")
    if user_guess.isdigit() == False:
        print("That doesn't look like a number. Please try again.")
        user_guess = input()
    if int(user_guess) == password: 
        print("Access granted.")
        break
    if guess_counter == 0:
        print("Sorry, you're out of guesses.")
        break
    elif int(pass_list[0])+ int(pass_list[2]) > 10:
        print("The first and last digits are both more than five.")
        guess_counter-=1
        print("Guesses left:", guess_counter)
        if guess_counter==0:
            print("Sorry, you're out of guesses.")
            break
    elif int(pass_list[0]) + int(pass_list[2]) == 10:
        print("The first and last digits of the password add up to 10.")
        guess_counter -=1
        print("Guesses left:", guess_counter)
        if guess_counter ==0:
            print("Sorry, you're out of guesses.")
            break
    else:
        print("The first and last digits of the password add up to ", int(pass_list[0])+int(pass_list[2]))
        guess_counter -=1
        print("Guesses left:", guess_counter)
        if guess_counter == 0:
            print("Sorry, you're out of guesses.")
            break
    user_guess = input("Guess again: ")
    if user_guess.isdigit() == False:
        print("That doesn't look like a number. Please try again.")
        user_guess = input()
