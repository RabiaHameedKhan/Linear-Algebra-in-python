import numpy as np

def diagonalize_matrix():
    print("Enter the 3x3 matrix A (row-wise, comma-separated):")

    A = []
    for i in range(3):
        row = list(map(float, input(f"Row {i+1}: ").split(',')))
        if len(row) != 3:
            print("Each row must have 3 values.")
            return
        A.append(row)

    A = np.array(A)
    print("\nMatrix A:")
    print(np.round(A, 4))

    # Step 1: Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)

    print("\nStep 1: Eigenvalues of A:")
    for i, val in enumerate(eigenvalues):
        print(f"λ{i+1} = {np.round(val, 4)}")

    print("\nStep 2: Eigenvectors of A:")
    for i in range(3):
        print(f"Eigenvector {i+1}: {np.round(eigenvectors[:, i], 4)}")

    # Step 3: Form the matrix P using eigenvectors as columns
    P = eigenvectors
    print("\nStep 3: Matrix P (formed using eigenvectors as columns):")
    print(np.round(P, 4))

    # Step 4: Inverse of P
    try:
        P_inv = np.linalg.inv(P)
    except np.linalg.LinAlgError:
        print("\nMatrix P is not invertible. Cannot diagonalize A.")
        return

    print("\nStep 4: Inverse of P (P⁻¹):")
    print(np.round(P_inv, 4))

    # Step 5: Diagonal matrix D = P⁻¹ * A * P
    D = np.dot(P_inv, np.dot(A, P))

    print("\nStep 5: Diagonal matrix D = P⁻¹ * A * P:")
    print(np.round(D, 4))

    print("\n✅ Matrix A has been successfully diagonalized.")

# Run the function
diagonalize_matrix()
 #testquestion: 4,1,1  
            #   0,2,0
            #   0,0,3