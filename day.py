# Ask the user for number of days
days = int(input("Enter number of days: "))

# Convert days to seconds
seconds = days * 24 * 60 * 60

# Display the result
print(f"{days} day(s) is equal to {seconds} seconds.")
