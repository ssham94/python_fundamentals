# Question 1
# You take the total and multiply it by 0.2 (for 20%) or other decimal places for how much you want to tip
total = 55
print("For 20% you should tip {}".format(total*0.2))

##################

# Question 2
# If we were to add a string and a int, it wouldn't work. We would have to convert the into into a string first with str(insert int here)
my_string = "hello world"
x = 3
x = str(x)
print(my_string + x)

##################

# Question 3
# We can either create a variable to store the operation, or we can directly type it into the string interpolation
y = 45628 * 7839
print("The total is {}".format(y))

##################

# Question 4
# The final result should be a True value. The first part of the expression should be a False value, but then the not(10 == 11) 
# will equal to True, therefore making it true
print((10 < 20 and 30 < 20) or not(10 == 11))