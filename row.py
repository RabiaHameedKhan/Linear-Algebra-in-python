import numpy as np

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

# Function to perform Gaussian elimination
def gaussian_elimination(A, B):
    n = len(A)
    augmented_matrix = np.hstack((A, B.reshape(-1, 1)))  # Augmented matrix
    
    # Forward elimination
    for i in range(n):
        if augmented_matrix[i, i] == 0:
            for j in range(i+1, n):
                if augmented_matrix[j, i] != 0:
                    augmented_matrix[[i, j]] = augmented_matrix[[j, i]]  # Swap rows
                    break
            else:
                return None  # No unique solution
        
        augmented_matrix[i] /= augmented_matrix[i, i]  # Make pivot 1
        
        for j in range(i+1, n):
            augmented_matrix[j] -= augmented_matrix[i] * augmented_matrix[j, i]

    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:n], x[i+1:n])

    return x

# Input the system of equations
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
    
    # Check consistency
    consistency, solution_type = check_consistency(A, B)
    
    if consistency == "inconsistent":
        print("\nThe system is **INCONSISTENT** (No solution exists).")
    else:
        print("\nThe system is **CONSISTENT**.")
        if solution_type == "finite":
            print("It has a **UNIQUE SOLUTION** (Finite).")
            result = gaussian_elimination(A, B)
            if result is not None:
                print("\nThe solution is:")
                for i, x in enumerate(result):
                    print(f"x{i+1} = {round(x, 4)}")
            else:
                print("Unexpected error occurred in solution computation.")
        else:
            print("It has **INFINITE SOLUTIONS** (Dependent system).")

# Run the program
if __name__ == "__main__":
    main()
