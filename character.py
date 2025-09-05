# Function to check if a character is uppercase or lowercase
def check_case(char):
    if char.isupper():
        return "Uppercase"
    elif char.islower():
        return "Lowercase"
    else:
        return "Not a letter"

# Main program
def main():
    char = input("Enter a single character: ")
    
    # Ensure only one character was entered
    if len(char) != 1:
        print("Please enter exactly one character.")
    else:
        result = check_case(char)
        print(f"The character '{char}' is {result}.")

# Run the program
main()
