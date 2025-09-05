# Program to input 5 values into an array and compute the average

def main():
    numbers = []  # empty list (array)

    # Loop to get 5 values
    for i in range(5):
        value = float(input(f"Enter value {i+1}: "))
        numbers.append(value)

    # Calculate average
    average = sum(numbers) / len(numbers)

    # Display results
    print("\nValues entered:", numbers)
    print(f"Average of the values: {average:.2f}")

# Run the program
main()
