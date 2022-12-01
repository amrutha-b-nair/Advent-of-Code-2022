
with open('input.txt') as file:
    calories = file.read().split('\n')

   
total_calories_elf = []
total_calorie = 0
# most_calories = 0

for calorie in calories:
    if calorie != "":
        total_calorie += int(calorie)
    else:
        total_calories_elf.append(total_calorie)
        # most_calories = max(most_calories, tot_calorie)
        total_calorie = 0

total_calories_elf.sort(reverse=True)

print("Part 1:", total_calories_elf[0])
print("Part 2:", sum(total_calories_elf[0:3]))
