import numpy as np

def gram_schmidt_process():
    n = int(input("Enter the number of vectors: "))
    dim = int(input("Enter the dimension of each vector: "))

    vectors = []
    for i in range(n):
        vec = list(map(float, input(f"Enter vector {i+1} (comma-separated): ").split(',')))
        if len(vec) != dim:
            print("Error: Each vector must have the specified dimension.")
            return
        vectors.append(np.array(vec))

    print("\nStep 1: Checking dot products to determine orthogonality:")
    is_orthogonal = True
    for i in range(n):
        for j in range(i+1, n):
            dot = np.dot(vectors[i], vectors[j])
            print(f"Dot(U{i+1}, U{j+1}) = {dot}")
            if not np.isclose(dot, 0):
                is_orthogonal = False

    if is_orthogonal:
        print("\n✅ Vectors are already orthogonal.")
    else:
        print("\n⏳ Vectors are not orthogonal. Applying Gram-Schmidt process...")

    # Step 2: Apply Gram-Schmidt to get orthogonal vectors
    orthogonal_vectors = []
    for i in range(n):
        vi = vectors[i]
        for j in range(i):
            proj = np.dot(vi, orthogonal_vectors[j]) / np.dot(orthogonal_vectors[j], orthogonal_vectors[j])
            vi = vi - proj * orthogonal_vectors[j]
        orthogonal_vectors.append(vi)

    print("\nStep 2: Orthogonal Vectors:")
    for i, vec in enumerate(orthogonal_vectors):
        print(f"V{i+1} = {np.round(vec, 4)}")

    # Step 3: Normalize orthogonal vectors to get orthonormal vectors
    orthonormal_vectors = []
    for vec in orthogonal_vectors:
        norm = np.linalg.norm(vec)
        if norm != 0:
            orthonormal_vectors.append(vec / norm)
        else:
            orthonormal_vectors.append(vec)

    print("\nStep 3: Orthonormal Vectors:")
    for i, vec in enumerate(orthonormal_vectors):
        print(f"Q{i+1} = {np.round(vec, 4)}")

    # Step 4: QR Decomposition
    Q = np.column_stack(orthonormal_vectors)
    A = np.column_stack(vectors)
    R = np.dot(Q.T, A)

    print("\nStep 4: QR Decomposition:")
    print("\nMatrix Q (from orthonormal vectors):")
    print(np.round(Q, 4))

    print("\nMatrix R = Qᵀ * A:")
    print(np.round(R, 4))

    print("\n✅ QR Decomposition completed successfully.")

# Run the function
gram_schmidt_process()
