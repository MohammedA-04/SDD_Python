# 1G Calling Another Function
# Function Life Expectancy Calculation

 #Function life expectancy calculation
def new_life (name, age):
    if smoker(name) == True:
        life_exp = 150
    else:
        life_exp = 200
    life_remaining = life_exp - age

    msg = "Hi "+name+"! Your new expected remaining life is: "+str(life_remaining)+" years."
    return msg

#Function for smoker database check
def smoker (name='', smoke=False):
    if name.capitalize() in ["Jane", "Zack", "Melissa"]:
        smoke = True
    return smoke

#Execution
print(new_life("jane", 30))
