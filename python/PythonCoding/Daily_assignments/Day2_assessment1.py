'''# Step 1: Create a list with 5 different types of fruits and print it
fruits = ["apple", "banana", "cherry", "mango", "kiwi"]
print("list of fruits:", fruits)

# Step 2: Add two more fruits to the list, remove one, and print the updated list
fruits.append("fig")
fruits.append("grape")
fruits.remove("mango")
print("Updated list of fruits:", fruits)

# Step 3: Access the second and fourth fruits in the list and print them
second_fruit = fruits[1]  # Index 1
fourth_fruit = fruits[3]  # Index 3
print("Second fruit:", second_fruit)
print("Fourth fruit:", fourth_fruit)

# Step 4: Slice the list to get the first three fruits and print the result
first_three_fruits = fruits[:3]
print("First three fruits:", first_three_fruits)

# Step 5: Find and print the length of the list
length_of_list = len(fruits)
print("Length of the list:", length_of_list)'''
'''# Step 1: Create a tuple with 3 cities and print it
cities = ("Paris", "Tokyo", "New York")
print("Original tuple of cities:", cities)

# Step 2: Access and print the first and last elements
first_city = cities[0]
last_city = cities[-1]
print("First city:", first_city)
print("Last city:", last_city)

# Step 3: Create another tuple with 2 more cities, concatenate, and print
more_cities = ("London", "Sydney")
all_cities = cities + more_cities
print("Concatenated tuple of cities:", all_cities)

# Step 5: Unpack the elements of the tuple into separate variables and print
city1, city2, city3 = cities
print("Unpacked cities:", city1, city2, city3)'''

'''# Step 1: Create a set of 5 unique colors and print it
colors = {"red", "blue", "green", "yellow", "purple"}
print("Original set of colors:", colors)

# Step 2: Add a new color and remove an existing color
colors.add("orange")      # Adding a new color
colors.remove("blue")     # Removing an existing color
print("Updated set of colors:", colors)

# Step 3: Create another set and perform intersection, union, and difference
more_colors = {"pink", "green", "black"}
intersection = colors.intersection(more_colors)
union =  colors.union(more_colors)
difference = colors.difference(more_colors)

print("Intersection:", intersection)
print("Union:", union)
print("Difference:", difference)

# Step 4: Check if a specific color is in the set
colors = {"red", "green", "yellow"}
# Check if "red" is in the set
print("red" in colors)

# Step 5: Convert a list of fruits with duplicates into a set and print unique fruits
fruits_list = ["apple", "banana", "apple", "cherry", "banana", "date"]
unique_fruits = set(fruits_list)
print("Unique fruits from the list:", unique_fruits)'''

# Step 1: Create a dictionary with name, age, and favorite hobby
my_info = {
    "name": "Alice",
    "age": 25,
    "favorite_hobby": "painting"
}
print("Original dictionary:", my_info)

# Step 2: Access and print the value associated with the name
print("Name:", my_info["name"])

# Step 3: Add favorite food and update favorite hobby
my_info["favorite_food"] = "pizza"           # Add new key-value pair
my_info["favorite_hobby"] = "reading"       # Update existing value
print("Updated dictionary:", my_info)

# Step 4: Print all keys and all values separately
print("Keys:", my_info.keys())
print("Values:", my_info.values())

# Step 5: Remove the age key-value pair and print the dictionary
my_info.pop("age")
print("Dictionary after removing age:", my_info)