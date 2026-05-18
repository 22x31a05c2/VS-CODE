# Get the number of values
n = int(input("Enter how many numbers: "))

# Get the numbers from the user
numbers = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate mean
mean = sum(numbers) / len(numbers)

# Print result
print("Mean:", mean)
