# Function to calculate area of a square
def area(side):
    return side ** 2

# Function to calculate perimeter of a square
def perimeter(side):
    return 4 * side

# Main program
def main():
    # Ask user for side length
    side = float(input("Enter the side length of the square: "))
    
    # Compute area and perimeter
    square_area = area(side)
    square_perimeter = perimeter(side)
    
    # Display results
    print(f"Area of the square: {square_area}")
    print(f"Perimeter of the square: {square_perimeter}")

# Run the program
main()
