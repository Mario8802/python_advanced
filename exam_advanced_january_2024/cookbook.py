from string import *


def cookbook(*args):

    cuisines_dict = {}

    for recipe_name_chef_alex, cuisine_of_chef_alex, ingredients_of_chef_alex in args:

        cuisines_dict.setdefault(cuisine_of_chef_alex, [])
        cuisines_dict[cuisine_of_chef_alex].append((recipe_name_chef_alex, ingredients_of_chef_alex))

    final_sortation_of_chef_alex = sorted(cuisines_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    end_result = ''


    for cuisine_of_chef_alex, secret_recipe_of_chef_alex in final_sortation_of_chef_alex:

        end_result += (f'{cuisine_of_chef_alex} cuisine contains'
                       f' {len(secret_recipe_of_chef_alex)} recipes:\n')

        sortation_of_recepies = sorted(secret_recipe_of_chef_alex, key=lambda x: x[0])

        for recipe in sortation_of_recepies:
            end_result += f'  * {recipe[0]} -> Ingredients: {", ".join(recipe[1])}\n'


    return end_result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))



#
# 3. Cookbook
#
# Alex is a passionate home chef with a diverse collection of recipes gathered from all corners of the globe.
# As he aspires to share his culinary creations with the world, his editor has tasked him with the challenging
# job of organizing these recipes into a coherent cookbook.

# Write a function called "cookbook" to assist Alex in arranging his recipes systematically. The function will receive
# a variable number of arguments, passed as tuples containing three elements: the first element is the recipe's name,
# the second is the cuisine, and the third is a list of ingredients e.g., ("Recipe Name", "Cuisine", ["Ingredient 1",
# "Ingredient 2"]).

# The objective is to sort the recipes by their cuisine, arranging Alex's collection based on the number of recipes in
# each cuisine in descending order. In cases where two or more cuisines have the same number of recipes, they should be
# returned in ascending order (alphabetically) by cuisine.

# Within each cuisine group, the recipes should be sorted in ascending order (alphabetically) by the recipe's name.
# To aid Alex in quickly assessing the number of recipes in each cuisine group, the function should print the count of
# recipes next to each cuisine. Furthermore, for each recipe within a cuisine group, display the necessary ingredients.
# In the end, return the output as described below.

# Note: Submit only the function in the judge system

# Input
#     • There will be no input from the console, just parameters passed to your function

# Output
#     • The output should look like this (before the star, there are two empty spaces.):

# "{cuisine_1} cuisine contains {number_of_recipes_in_the_cuisine_group} recipes:
#   * {recipe_name_1} -> Ingredients: {ingredient_1}, {ingredient_2}, ...
#   * {recipe_name_2} -> Ingredients: {ingredient_1}, {ingredient_2}, ...
#   ...

#   * {recipe_name_n} -> Ingredients: {ingredient_1}, {ingredient_2}, ...
# {cuisine_2} cuisine contains {number_of_recipes_in_the_cuisine_group} recipes:
#   * {recipe_name_1} -> Ingredients: {ingredient_1}, {ingredient_2}, ...
#   ...

#   * {recipe_name_n} -> Ingredients: {ingredient_1}, {ingredient_2},
#   ... {cuisine_n} cuisine contains {number_of_recipes_in_the_cuisine_group} recipes:
#   * {recipe_name_1} -> Ingredients: {ingredient_1}, {ingredient_2}, ..."
# Constraints
#     • Each tuple provided will always contain a unique recipe and its associated cuisine.
#     • Alex will never receive the same recipe twice or more in the given input.
#     • The list of ingredients for each recipe will never be empty.