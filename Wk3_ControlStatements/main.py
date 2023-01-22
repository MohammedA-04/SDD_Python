print(' Welcome back to school! Answer these 3 questions to introduce yourself!')
name: str = input('What is your name?')
print(name)

favorite_color = input('What is your favorite color?')
print(favorite_color)
favorite_tv_show = input('What is your favorite TV?')
print(favorite_tv_show)
favorite_driver = input('What is your favorite driver?')
print(favorite_driver)

print(f"Everyone,meet{name}!{name}'s favorite color is{favorite_color}.{name}'s favorite tv show is{favorite_tv_show}."
      f"{name}'s driver is = {favorite_driver}")

# This is to have on different lines
# print(f"Everyone,meet{name}!{name}'s favorite color is{favorite_color}.")
# print(f"{name}'s favorite tv show is{favorite_tv_show}.")
# print(f"{name}'s driver is = {favorite_driver}")