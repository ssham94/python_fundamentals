# Exercise 4.4
secret_number = 13

print("Try to guess my secret number")

number_guess = input()
number_guess = int(number_guess)

if secret_number == number_guess:
    print("You win!")
elif abs(secret_number - number_guess) == 1:
    print("So close!")
else:
    print("Try again")