
with open('input.txt') as file:
    calories = file.read().split('\n')

   
elf_calories = []
total_calorie = 0

# most_calories = 0

for calorie in calories:
    if calorie != "":
        total_calorie += int(calorie)
    else:
        elf_calories.append(total_calorie)
        # most_calories = max(most_calories, tot_calorie)
        total_calorie = 0

elf_calories.sort(reverse=True)

# print("Part 1:", most_calories)

print("Part 1:", elf_calories[0])
print("Part 2:", sum(elf_calories[0:3]))
