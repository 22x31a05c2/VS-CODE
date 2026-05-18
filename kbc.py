# Creating questions manually using a list
# Each question is a list containing:
# [question, option1, option2, option3, option4, extra(not used), correct_option_number]

questions = [
    ["by which language the facebook is written", "python", "java script", "mern", "html", "none", 4],
    ["by which language the youtube is written", "python", "java script", "mern", "html", "none", 4],
    ["by which language the facebook is written", "python", "java script", "mern", "html", "none", 4],
    ["by which language the facebook is written", "python", "java script", "mern", "html", "none", 4],
    ["by which language the facebook is written", "python", "java script", "mern", "html", "none", 4],
    ["by which language the facebook is written", "python", "java script", "mern", "html", "none", 4],
    ["by which language the facebook is written", "python", "java script", "mern", "html", "none", 4],
    ["by which language the facebook is written", "python", "java script", "mern", "html", "none", 4],
    ["by which language the facebook is written", "python", "java script", "mern", "html", "none", 4],
    ["by which language the facebook is written", "python", "java script", "mern", "html", "none", 4],
    ["by which language the facebook is written", "python", "java script", "mern", "html", "none", 4],
    ["by which language the facebook is written", "python", "java script", "mern", "html", "none", 4],
    ["by which language the facebook is written", "python", "java script", "mern", "html", "none", 4],
]

# Money levels for each question
# levels[i] represents the prize money for question i
levels = [1000, 2000, 3500, 4500, 10000, 15000, 17500, 250000]

# Variable to store the guaranteed take-away money
money = 0

# Loop through all the questions using index i
for i in range(0, len(questions)):

    # Get the current question
    question = questions[i]

    # Print the prize money for the current question
    print(f"Question for rs.{levels[i]}")

    # Print the actual question text
    print(f"The question is {question[0]}")

    # Print the options
    print(f" a. {question[1]}            b. {question[2]}")
    print(f" c. {question[3]}            d. {question[4]}")

    # Take user input (1 to 4)
    reply = int(input("enter the option in 1 to 4: "))

    # Check if the answer is correct
    if reply == question[-1]:

        # Correct answer message
        print(f"congratulations's, you have won {levels[i]}")

        # Setting guaranteed money at certain safe levels
        if i == 4:        # After 5th question
            money = 10000
        elif i == 9:      # After 10th question
            money = 320000
        elif i == 14:     # After 15th question
            money = 1000000

    else:
        # If the answer is wrong
        print(f"wrong answer: {reply}")
        break  # Exit the quiz loop

# Print the final take-away money
print(f"ur take away money is {money}")