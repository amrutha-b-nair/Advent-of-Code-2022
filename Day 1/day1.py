with open('input.txt') as f:
    cal = f.readlines()

calories = []
for i in cal:
    calories.append(i.strip())
    

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

# print(total_calories)
total_calories.sort(reverse=True)

print(sum(total_calories[0:3]))
