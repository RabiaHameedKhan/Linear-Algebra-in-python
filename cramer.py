import numpy as np

# Function to calculate the determinant of a matrix
def calculate_determinant(matrix):
    return round(np.linalg.det(matrix), 4)  # Round for better precision

# Function to check system consistency
def check_consistency(A, B):
    augmented_matrix = np.hstack((A, B.reshape(-1, 1)))  # Combine A and B into an augmented matrix
    
    rank_A = np.linalg.matrix_rank(A)
    rank_aug = np.linalg.matrix_rank(augmented_matrix)
    
    if rank_A == rank_aug:
        if rank_A == len(A):  # Full rank (Unique solution)
            return "consistent", "finite"
        else:
            return "consistent", "infinite"
    else:
        return "inconsistent", None

# Function to apply Cramer's Rule
def cramers_rule(A, B):
    det_A = calculate_determinant(A)

    if det_A == 0:
        consistency, solution_type = check_consistency(A, B)
        
        if consistency == "inconsistent":
            return "The system is **INCONSISTENT** (No solution exists)."
        else:
            return "The system is **CONSISTENT** with **INFINITE SOLUTIONS** (Dependent system)."
    
    n = len(A)
    solutions = []

    for i in range(n):
        A_copy = A.copy()
        A_copy[:, i] = B  # Replace the i-th column with vector B
        det_Ai = calculate_determinant(A_copy)
        solutions.append(round(det_Ai / det_A, 4))

    return solutions

# Function to input the system of equations
def input_system():
    n = int(input("Enter the number of variables: "))
    A = []
    B = []
    
    print(f"Enter the coefficients of the {n} equations:")
    for i in range(n):
        equation = list(map(float, input(f"Enter coefficients for equation {i+1} (separated by spaces): ").split()))
        
        while len(equation) != n + 1:
            print(f"Error: Please enter exactly {n} coefficients followed by the right-hand side value.")
            equation = list(map(float, input(f"Re-enter coefficients for equation {i+1}: ").split()))
        
        A.append(equation[:-1])  # Coefficients of the variables
        B.append(equation[-1])   # Right-hand side values
    
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    
    return A, B

# Main function
def main():
    A, B = input_system()
    
    # Apply Cramer's Rule
    result = cramers_rule(A, B)
    
    # Output the result
    if isinstance(result, str):
        print("\n" + result)
    else:
        print("\nThe system is **CONSISTENT** with a **UNIQUE SOLUTION**:")
        for i, x in enumerate(result):
            print(f"x{i+1} = {x}")

# Run the program
if __name__ == "__main__":
    main()
