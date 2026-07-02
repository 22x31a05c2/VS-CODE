original_number='123'
guess_number=input("Enter The Guessing Number: ")

if len(original_number)!=len(guess_number):
    print(f"Enter {len(original_number)} number")
if len(original_number)!=len(set(guess_number)):
    print("Duplicate number")

if (int(original_number)-int(guess_number)==0):
    print("FERMI"*len(original_number))
    print("***YOU WON***")

output=[]
for i in range(len(original_number)):
    for j in range(len(guess_number)):
        if original_number[i]==guess_number[j]:
            output.append('FERMI')
        else:
            output.append('PICO')

output_string=''
for item in output:
    output_string=output_string+' '+item

if len(output)==0:
    print('BAGEL')
else:
    print(output_string)