from tkinter import *
from tkinter import ttk

all_meals = []
total_calories = []
total_protein = []
num_meals = 0 


moreMeals = input("Would you like to enter a meal? (Yes/No)")
while moreMeals == "Yes":
        meal = input("what was your meal: ")
        all_meals.append(meal)
        print(all_meals)
        calories = float(input("How many calories did your first meal have: "))
        total_calories.append(calories)
        print(total_calories)
        protein = float(input("How much protein did your first meal have? "))
        total_protein.append(protein)
        print(total_protein)
        break

moreMeals = input("Would you like to enter another meal?")
while moreMeals == "Yes":
        meal = input("what was your meal: ")
        all_meals.append(meal)
        print(all_meals)
        calories = float(input("How many calories did your first meal have: "))
        total_calories.append(calories)
        print(total_calories)
        protein = float(input("How much protein did your first meal have? "))
        total_protein.append(protein)
        print(total_protein)
        break

print(all_meals)
print(total_calories)
print(total_protein)



