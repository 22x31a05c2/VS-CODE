def reverse_integer(n):
    # Check if the number is negative
    is_negative = n < 0
    
    # Convert the integer to string and reverse it
    reversed_str = str(abs(n))[::-1]
    
    # Convert the reversed string back to integer
    reversed_int = int(reversed_str)
    
    # Restore the negative sign if necessary
    if is_negative:
        reversed_int = -reversed_int
    
    return reversed_int

# Input from the user
try:
    user_input = int(input("Enter an integer to reverse: "))
    reversed_number = reverse_integer(user_input)
    print(f"The reversed integer is: {reversed_number}")
except ValueError:
    print("Please enter a valid integer.")