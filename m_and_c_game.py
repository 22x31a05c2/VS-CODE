# missionaries and cannibals game
boat_side="Right"
Missionaries_on_right= 3
Cannibals_on_right= 3
Missionaries_on_left= 0
Cannibals_on_left= 0
print('M=',Missionaries_on_left,'C=',Cannibals_on_left,'|----------B|','M=',Missionaries_on_right,'C=',Cannibals_on_right)

# PART 2
missionaries=int(input("enter the no of missionaries>3 : "))
cannibals=int(input("enter the no of cannibals >3 : "))

# CREATE A LOOP FOR NO OF MISS AND CANN
if (missionaries + cannibals) != 1 and  (missionaries + cannibals) !=2:
    print("Invalid Move")

# boat loop
if boat_side=="Right":
    print(f"Boat is on {boat_side}",'|----------B|')
else:
    print("Boat is on left side",'|B----------|')
