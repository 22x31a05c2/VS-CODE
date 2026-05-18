def number_to_words(n):
    """Convert an integer n to its English words representation."""
    if n < 0:
        return "negative " + number_to_words(-n)
    elif n == 0:
        return "zero"
    
    words = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }
    
    if n < 21:
        return words[n]
    elif n < 100:
        return words[n // 10 * 10] + ('' if n % 10 == 0 else ' ' + words[n % 10])
    elif n < 1000:
        return words[n // 100] + " hundred" + ('' if n % 100 == 0 else ' and ' + number_to_words(n % 100))
    else:
        return "Number too large"

def read_integer_from_file(filename):
    """Read an integer from a file."""
    with open(filename, 'r') as file:
        return int(file.read().strip())

def write_to_file(filename, content):
    """Write content to a file."""
    with open(filename, 'w') as file:
        file.write(content)

def main():
    filename = 'number.txt'  # Replace with your filename
    try:
        # Read the integer from the file
        number = read_integer_from_file(filename)
        
        # Convert the integer to words
        words = number_to_words(number)
        
        # Prepare the result string
        result = f"{number} {words}"
        
        # Write the result back to the file
        write_to_file(filename, result)
        
        print(f"Written to file: {result}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except ValueError:
        print("The file does not contain a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()