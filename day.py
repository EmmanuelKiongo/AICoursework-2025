# Ask the user for number of days
Days = int(input("Enter number of days: "))

# Convert days to seconds
seconds = Days * 24 * 60 * 60

# Display the result
print(f"{Days} day(s) is equal to {seconds} seconds.")
