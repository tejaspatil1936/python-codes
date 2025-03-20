# Defining sets
vegetarian_dishes = {"Salad", "Paneer Tikka", "Veg Biryani", "Pasta"}
non_vegetarian_dishes = {"Chicken Biryani", "Fish Curry", "Pasta", "Egg Curry"}

# Finding all available dishes (union)
all_dishes = vegetarian_dishes | non_vegetarian_dishes  # Using union operator
print("All available dishes:", all_dishes)

# Finding common dishes (intersection)
common_dishes = vegetarian_dishes & non_vegetarian_dishes  # Using intersection operator
print("Common dishes in both sets:", common_dishes)

# Checking if vegetarian_dishes is a subset of non_vegetarian_dishes
is_subset = vegetarian_dishes.issubset(non_vegetarian_dishes)
print("Is vegetarian_dishes a subset of non_vegetarian_dishes?", is_subset)
