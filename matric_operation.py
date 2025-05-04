import numpy as np

def get_matrix(rows, cols, name="Matrix"):
    """Function to take matrix input from the user."""
    print(f"\nEnter elements for {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print(f"Error: Please enter exactly {cols} values.")
            return get_matrix(rows, cols, name)
        matrix.append(row)
    return np.array(matrix)

def matrix_operations():
    """Main function to perform matrix operations."""
    print("Matrix Operations: Addition (+), Subtraction (-), Multiplication (*)")
    
    # Get dimensions
    rows = int(input("Enter number of rows for Matrix A: "))
    cols = int(input("Enter number of columns for Matrix A: "))
    
    A = get_matrix(rows, cols, "Matrix A")
    
    rows_B = int(input("Enter number of rows for Matrix B: "))
    cols_B = int(input("Enter number of columns for Matrix B: "))
    
    B = get_matrix(rows_B, cols_B, "Matrix B")
    
    # Ask for operation
    operation = input("Choose operation (+, -, *): ").strip()
    
    try:
        if operation == "+":
            if A.shape == B.shape:
                result = A + B
            else:
                print("Error: Matrices must have the same dimensions for addition.")
                return
        elif operation == "-":
            if A.shape == B.shape:
                result = A - B
            else:
                print("Error: Matrices must have the same dimensions for subtraction.")
                return
        elif operation == "*":
            if A.shape[1] == B.shape[0]:  # Check if multiplication is possible
                result = np.dot(A, B)
            else:
                print("Error: Number of columns in A must equal the number of rows in B for multiplication.")
                return
        else:
            print("Invalid operation selected.")
            return
        
        print("\nResultant Matrix:")
        print(result)
    
    except Exception as e:
        print("Error:", e)

# Run the program
if __name__ == "__main__":
    matrix_operations()
