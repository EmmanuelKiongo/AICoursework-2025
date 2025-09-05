import math

# Ask the user to input the radius
radius = float(input("Enter the radius of the sphere: "))

# Calculate the volume of the sphere
volume = (4/3) * math.pi * (radius ** 3)

# Display the result
print(f"The volume of a sphere with radius {radius} is {volume:.2f}")
