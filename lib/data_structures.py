spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
 return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None
american_food = get_spicy_food_by_cuisine(spicy_foods, "American")
print("American food:", american_food)

thai_food = get_spicy_food_by_cuisine(spicy_foods, "Thai")
print("Thai food:", thai_food)

def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    for food in spiciest:
        heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")


def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    average_heat = total_heat / len(spicy_foods)
    return average_heat
print_spiciest_foods(spicy_foods)
average_heat = get_average_heat_level(spicy_foods)
print("Average heat level:", average_heat)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
new_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}
updated_spicy_foods = create_spicy_food(spicy_foods, new_food)
print(updated_spicy_foods)
