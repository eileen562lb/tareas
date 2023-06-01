# Pizza -- string concatenation
# 
# Combine the strings below to make a sentence that says:
# "Hello, I'm trying to order an large pizza with mushrooms pepperoni and extra cheese."
# 
# The variables named first_topping, second_topping, and third_topping are already defined.
# You just have to combine them to make a string.
# if you need help, see this page:
# https://www.w3schools.com/python/gloss_python_string_concatenation.asp

first_topping, second_topping, third_topping = ["mushrooms", "pepperoni","extra cheese"] # do not change

# you can change this line
result = "Hello, I'm trying to order an large pizza with."

#Do not change the code below
good_result = "Hello, I'm trying to order an large pizza with mushrooms pepperoni and extra cheese."
if result != good_result:
    raise Exception(f"Expected:\n{good_result} but got \n{result}.")