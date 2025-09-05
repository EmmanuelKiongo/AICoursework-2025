# Program to input 5 values into an array and compute the average

def main():
    Numbers = []  # empty list (array)

    # Loop to get 5 values
    for i in range(5):
        value = float(input(f"Enter value {i+1}: "))
        Numbers.append(value)

    # Calculate average
    average = sum(Numbers) / len(Numbers)

    # Display results
    print("\nValues entered:", Numbers)
    print(f"Average of the values: {average:.2f}")

# Run the program
main()
