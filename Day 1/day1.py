with open('input.txt') as file:
    calories = file.read().split('\n')

   
total_calories = []
tot_calorie = 0
# most_calories = 0

for calorie in calories:
    if calorie != "":
        tot_calorie += int(calorie)
    else:
        total_calories.append(tot_calorie)
        # most_calories = max(most_calories, tot_calorie)
        tot_calorie = 0

total_calories.sort(reverse=True)

print("Part 1:", total_calories[0])
print("Part 2:", sum(total_calories[0:3]))
