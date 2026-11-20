radius = float(input("Enter the radius of the circle: "))
area = 3.14159 * radius ** 2
print(f"The area of the circle with radius {radius} is {area:.2f}")
# A pitfall of this code is that it does not handle negative radius values. If the user enters a negative radius, the area will still be calculated, which does not make sense in the context of a circle.