# Author: Vansh Nibhoria
# Date: 03/10/2025
# Project: Daily calorie tracker

print("=====================================")
print("welcome to the Daily Calorie Tracker!")
print("=====================================")
print("This tool helps you log and monitor your daily calorie intake.")
print("you can enter your meals and calories,and review your progress.")
print("let's get started!\n")



meal_list = []
calorie_list = []


meal_count = int(input("How many meals would you like to enter today"))


for n in range(meal_count):
    print(f"\nMeal {n+1}")
    meal = input("Enter meal name")
    calories = float(input("Enter calorie amount: "))

meal_list.append(meal)
calorie_list.append(calories)


total_calories = sum(calorie_list)
avg_calories = total_calories/meal_count

print("\nTotal Calories : {total_calories}")
print("Average per meal:{avg_calories:.2f}")



daily_limit = float(input("\nEnter your daily limit: "))

if total_calories > daily_limit:
    print(f"you exceeded your daily limit by {total_calories-daily_limit}cal.")
elif total_calories < daily_limit:
    print(f"you are {daily_limit-total_calories} calories under your limit.GJ")
else:
    print("Perfect! you hit your daily calorie limit exactly.")

print("Thank you")