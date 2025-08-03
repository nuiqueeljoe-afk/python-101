# The Cyclone 🎢
# Codédex

height = int(input('What is your height (cm)?'))
credits = int(input('How many credits do you have?'))

if height >= 137 and credits >= 10:
  print('Enjoy the ride')
elif height < 137 and credits > 10:
  print('You are not tall enought to ride')
elif height > 137 and credits < 10:
  print('You dont have enought credits')
else:
  print('they have not met either requirements')
#so when you input both 137 and 10 it will execute "Enjoy the ride"
