##################
# APP fun age game
#################

print('welcome to my first app in python language coding')
print('#' * 80)
yourname = input(' what\'s your name ?').strip().capitalize()
yourage = input('please input your age : ')
months = 12
weeks = 48
days = weeks * 31 
hours = days * 24
minutes = hours * 60


print(f'thank you to use my app')
print('this is not integer, please write your age')
print(f'hello ,{yourname} your in months {int(yourage) * 12} and in weeks {int(yourage) * weeks} and days {int(yourage) * days} and in hours {int(yourage) * hours} and minutes {int(yourage) * minutes} ')
print('#' * 80)
