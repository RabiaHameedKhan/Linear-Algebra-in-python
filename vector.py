import numpy as np

def vector_operations():
    # Input vectors from the user
    v1 = np.array(list(map(float, input("Enter the first vector (comma-separated): ").split(','))))
    v2 = np.array(list(map(float, input("Enter the second vector (comma-separated): ").split(','))))
    
    # Ensure both vectors are of the same size
    if v1.shape != v2.shape:
        print("Vectors must be of the same dimension!")
        return

    # Addition
    addition = v1 + v2
    print(f"Vector Addition: {addition}")

    # Subtraction
    subtraction = v1 - v2
    print(f"Vector Subtraction: {subtraction}")

    # Dot Product
    dot_product = np.dot(v1, v2)
    print(f"Dot Product: {dot_product}")

    # Cross Product (only for 3D vectors)
    if len(v1) == 3 and len(v2) == 3:
        cross_product = np.cross(v1, v2)
        print(f"Cross Product: {cross_product}")
    else:
        print("Cross product is only defined for 3D vectors.")

# Run the program
vector_operations()
