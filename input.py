# Get a list of names from the user
names_input = input("Enter names separated by commas: ")

# Split the input string into a list
names_list = names_input.split(',')

# Capitalize the first letter of each name and strip any extra whitespace
capitalized_names = [name.strip().capitalize() for name in names_list]

# Print the list of capitalized names
print(capitalized_names)