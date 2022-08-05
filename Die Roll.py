# Imports
import random

# Variables
number_of_dice = int(input("Enter the number of dice to be thrown: "))
if number_of_dice == "" or number_of_dice == 0:
	number_of_dice = 1
number_of_sides = int(input("Enter the number of sides the die has: "))
number_of_rolls = int(input("Enter the number of times you want to roll the die/s: "))
divider = []
sequence = []
count = {}
dice = 1


# Solver
for side in range(1, number_of_sides + 1):
	count[side] = 0

for roll in range(number_of_rolls * number_of_dice):
	result = random.randint(1, number_of_sides)
	count[result] += 1
	divider.append(result)
	if dice == number_of_dice:
		sequence.append(divider[:])
		divider.clear()
		dice = 0
	dice += 1


print(sequence)
print(count)
