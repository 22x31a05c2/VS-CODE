# missionaries and cannibals game
boat_side = "Right"
Missionaries_on_right = 3
Cannibals_on_right = 3
Missionaries_on_left = 0
Cannibals_on_left = 0

def print_state():
    """Display current state of the game"""
    if boat_side == "Right":
        print(f'M={Missionaries_on_left} C={Cannibals_on_left} |----------B| M={Missionaries_on_right} C={Cannibals_on_right}')
    else:
        print(f'M={Missionaries_on_left} C={Cannibals_on_left} |B---------- M={Missionaries_on_right} C={Cannibals_on_right}')

def is_valid_state():
    """Check if current state is valid (cannibals don't outnumber missionaries on either side)"""
    # Left side check
    if Missionaries_on_left > 0 and Cannibals_on_left > Missionaries_on_left:
        return False
    # Right side check
    if Missionaries_on_right > 0 and Cannibals_on_right > Missionaries_on_right:
        return False
    return True

def check_win():
    """Check if game is won"""
    if Missionaries_on_left == 3 and Cannibals_on_left == 3 and boat_side == "Left":
        return True
    return False

print_state()

# Main game loop
while True:
    print("\n--- Make a move ---")
    missionaries = int(input("Enter the no of missionaries to move (0-3): "))
    cannibals = int(input("Enter the no of cannibals to move (0-3): "))
    
    # Validate the move (1-2 people per trip)
    if (missionaries + cannibals) < 1 or (missionaries + cannibals) > 2:
        print("Invalid Move! You can move 1 or 2 people only")
        continue
    
    # Move people based on boat side
    if boat_side == "Right":
        # Moving from right to left
        if missionaries > Missionaries_on_right or cannibals > Cannibals_on_right:
            print("Not enough people on the right side!")
            continue
        
        Missionaries_on_right -= missionaries
        Cannibals_on_right -= cannibals
        Missionaries_on_left += missionaries
        Cannibals_on_left += cannibals
        boat_side = "Left"
    else:
        # Moving from left to right
        if missionaries > Missionaries_on_left or cannibals > Cannibals_on_left:
            print("Not enough people on the left side!")
            continue
        
        Missionaries_on_left -= missionaries
        Cannibals_on_left -= cannibals
        Missionaries_on_right += missionaries
        Cannibals_on_right += cannibals
        boat_side = "Right"
    
    # Check if the move is valid
    if not is_valid_state():
        print("Invalid state! Cannibals outnumber missionaries. Game Over!")
        break
    
    print_state()
    
    # Check if won
    if check_win():
        print("\n🎉 Congratulations! You won! All missionaries and cannibals are on the left side!")
        break