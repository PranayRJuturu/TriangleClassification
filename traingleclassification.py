import math
import mybrand

def is_right_angled(a, b, c):  # Checks whether the triangle is right-angled
    asq = float(math.pow(a, 2))  # Square of the lengths of the sides
    bsq = float(math.pow(b, 2))
    csq = float(math.pow(c, 2))

    # Using Pythagoras theorem to verify if the triangle is right-angled
    if (asq + bsq == csq) or (bsq + csq == asq) or (csq + asq == bsq):
        return True
    else:
        return False


def classify_triangle(a, b, c):
   
    if a == 0 or b == 0 or c == 0:
        return "Invalid lengths"

    if a == b == c:

        return "The triangle is Equilateral"  # Equilateral triangles cannot be right-angled

    elif a == b or b == c or c == a:

        if is_right_angled(a, b, c):
            return "The triangle is Right-angled"
        else:
            return "The triangle is Isosceles"

    else:

        if is_right_angled(a, b, c):
            return "The triangle is Right-angled"
        else:
            return "The triangle is Scalene"

try:

    side_1 = float(input("Enter the length of the side 1:"))
    side_2 = float(input("Enter the length of the side 2:"))
    side_3 = float(input("Enter the length of the side 3:"))
    
    print(classify_triangle(side_1, side_2, side_3))
    mybrand.my_brand("Triangle Classification")

except ValueError:
    print("Input should be numerical!")