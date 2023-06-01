import calendar
def findDay(day:int, month:int, year:int):print("That day was a " + (["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"].copy()[calendar.weekday(year, month, day)]))

# Calling Functions - what day were you born?
# 
# Using the input function, ask the user what day, month, and year they were born.
# 
# Then call the function findDay that takes three inputs: day, month, year.
# You don't have to call them day, month, and year, but you can if you want.
# 

#your code here
# findDay(day, month, year)