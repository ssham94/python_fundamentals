# Exercise 4.2
print("How old are you?")
user_age = input()
user_age = int(user_age)

if user_age > 105:
    print("I'm not sure I believe you")
else:
    print("We are {} years apart".format(abs(user_age-25)))