# Activity 3A - Produce this Ans:  y= 6x **2 + 3x + 2  for X = 2
def f(x):
    return 6 * x ** 2 + 3 * x + 2

print(f(2))

# Acitivty 3B - Def function shut down
def shutdown(s):
    if s == "Yes":
        return "Shutting Down"
    elif s == "No":
        return "Shutdown Aborted"
    else:
        return "Sorry"
print(shutdown("Yes"))

# Acitivty 3C -
def distance_from_zero(Number):
   if type(Number) == int or type(Number) == float:
       return abs(Number)
   else:
       return "Nope"

print(distance_from_zero(-5)) #Silly me i was using Number to print LOL:) 1/2 hr
print(distance_from_zero("What\n"))

# Activity 3D
"""
Hours = print(input("\nEnter Hours:"))
Rate  = print(input("Enter Rate :"))
Pay   = """

"""
HourInput = input("\nEnter Hours:")
Hr = float(HourInput)

RateInput = input("Enter the Rate:")
Rate = float(RateInput)
if Hr <= 40:
 	print( Hr * Rate) # if > or = 40 | 45 * 10 = 450
elif Hr > 40: # 45 hrs
	print( (40 * Rate) + ( (Hr-40) * 1.5 * Rate) )
"""
# Part 2 in defintion decomposed using 2 paramneter and handle excpeoitn
def computepay(hours, rate) :
   return hours * rate
def invalid_input() :
   print("Input Numeric Value")
while True:
   try:
      regular_rate = float(input("Hourly rate in dollars: "))
      break
   except:
      invalid_input()
      continue
while True:
   try:
      regular_hours = float(input("Regular Hours Worked: "))
      break
   except:
      invalid_input()
      continue
while True:
   try:
      overtime_hours = float(input("Overtime hours worked :"))
      break
   except:
      invalid_input()
      continue

overtime_rate = regular_rate * 1.5
regular_pay = computepay(regular_hours, regular_rate)
overtime_pay = computepay(overtime_hours, overtime_rate)
total_pay = regular_pay + overtime_pay
print("PAY : ", total_pay)