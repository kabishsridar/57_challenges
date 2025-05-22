length = int(input("Enter the length of ceiling(sq feet): ")) # prompt for length
width = int(input("Enter the width of ceiling(sq feet): ")) # prompt for width
gallon = 350 # initiating gallon as 350 as one gallon covers 350 sq feet
area = length * width # calculatiing and storing area of ceiling

num_gallon = (area // gallon ) + 1 # we need 1 complete gallon extra if even for 351 sq feets, two gallons are required

# displaying the final output
print(f"You will need to purchase {num_gallon} gallons of paint \nto cover {area} square feet. ")