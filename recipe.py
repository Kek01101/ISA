import json
import requests
import sys
from copy import deepcopy

# Api ids and keys necesary for forming query, url is included as well
api_id = "0bdc8911"
api_key = "8a4e1e022c96a4d6753c7278f84bb80d"
url = "https://api.edamam.com/search"

# Forming the request for the website - 'ingr':'Ingredient length goes here'
payload1 = {'q':'ingredients go here', 'app_id':api_id, 'app_key':api_key, 'ingr':'Ingredient length goes here'}
payload2 = {'q':'ingredients go here', 'app_id':api_id, 'app_key':api_key, 'ingr':'Ingredient length+1 goes here'}

# Input in list format here
ingredients = input("Please input all ingredients, seperated by commas:\n").lower()

# Formatting requests for sending to API
payload1['q'] = ingredients
payload1['ingr'] = len(ingredients.split(", "))
payload2['q'] = ingredients
payload2['ingr'] = len(ingredients.split(", "))+1

# Sending off request and saving response to r1 and r2
r1 = requests.get(url, params=payload1)
r2 = requests.get(url, params=payload2)

# Cleaning up the response and saving valid recipes to 'recipes' array
r_json = r1.json()
r_json = r_json['hits']
recipes = []
for thing in r_json:
    recipes.append(thing["recipe"])
if len(recipes) == 0:
    print("[SORRY] There are no available recipes for those ingredients")
    sys.exit()
r_json = r2.json()
r_json = r_json['hits']
recipes2 = []
for thing in r_json:
    recipes2.append(thing["recipe"])

# Cleaning up recipes 2 to not include things in recipes
for thing in deepcopy(recipes2):
    if thing in recipes:
        recipes2.remove(thing)

# Recipe manipulation below
# name of recipe --> label
# Ingredients --> ingredientLines
print("We found these available recipes:")
for a in range(len(recipes)):
    print(f"[{a+1}]: {recipes[a]['label']}")
print(f"[{a+2}]: We found {len(recipes2)} more recipes using 1 more ingredient!")

# User chooses a recipe
extra_choice = False
correct = False
while not correct:
    choice = int(input("\nInsert the number of a recipe to learn more, 0 to exit: "))
    if choice == 0:
        sys.exit()
    elif choice-1 < len(recipes):
        correct = True
    elif choice-1 == len(recipes):
        if not extra_choice:
            extra_choice = True
            for a in range(len(recipes2)):
                print(f"[{a+1}]: {recipes2[a]['label']}")

# Program outputs recipe
if extra_choice:
    print(recipes2[choice - 1]['label'] + ":")
    for ingredient in recipes2[choice - 1]['ingredientLines']:
        print(ingredient)
    print("Instructions here: " + recipes2[choice - 1]['url'])
else:
    print(recipes[choice-1]['label'] + ":")
    for ingredient in recipes[choice-1]['ingredientLines']:
        print(ingredient)
    print("Instructions here: " + recipes[choice-1]['url'])