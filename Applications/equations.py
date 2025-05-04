import re
import numpy as np
from fractions import Fraction


def parse_compound(compound):
    elements = re.findall(r'([A-Z][a-z]*)(\d*)', compound)
    parsed = {}
    for (element, count) in elements:
        parsed[element] = parsed.get(element, 0) + int(count or 1)
    return parsed

def parse_side(side):
    compounds = side.split('+')
    return [parse_compound(compound.strip()) for compound in compounds]

def get_elements(compounds):
    elements = set()
    for compound in compounds:
        elements.update(compound.keys())
    return sorted(elements)

def form_matrix(lhs, rhs, elements):
    matrix = []
    for element in elements:
        row = []
        for compound in lhs:
            row.append(compound.get(element, 0))
        for compound in rhs:
            row.append(-compound.get(element, 0))
        matrix.append(row)
    return matrix

def gaussian_elimination(matrix):
    matrix = np.array(matrix, dtype=float)
    rows, cols = matrix.shape

    for i in range(rows):
        # Make the diagonal element 1
        if matrix[i][i] == 0:
            for j in range(i+1, rows):
                if matrix[j][i] != 0:
                    matrix[[i, j]] = matrix[[j, i]]
                    break

        matrix[i] = matrix[i] / matrix[i][i]
        
        for j in range(i+1, rows):
            matrix[j] = matrix[j] - matrix[i] * matrix[j][i]

    # Back substitution
    x = np.zeros(cols)
    for i in range(rows-1, -1, -1):
        x[i] = matrix[i][-1]
        for j in range(i+1, cols-1):
            x[i] -= matrix[i][j] * x[j]

    # Handling free variables by assigning 1
    x = x[:cols-1]
    lcm = np.lcm.reduce([Fraction(f).limit_denominator().denominator for f in x])
    x = (x * lcm).round().astype(int)
    x = np.append(x, lcm)

    return x

def balance_chemical_equation(equation):
    lhs, rhs = equation.split('->')
    lhs_compounds = parse_side(lhs)
    rhs_compounds = parse_side(rhs)
    elements = get_elements(lhs_compounds + rhs_compounds)

    matrix = form_matrix(lhs_compounds, rhs_compounds, elements)

    # Add an extra equation for normalization
    matrix.append([1] * (len(lhs_compounds) + len(rhs_compounds)))

    coeffs = gaussian_elimination(matrix)

    # Output the balanced equation
    lhs_result = []
    for coeff, compound in zip(coeffs[:len(lhs_compounds)], lhs.split('+')):
        lhs_result.append(f"{coeff if coeff != 1 else ''}{compound.strip()}")

    rhs_result = []
    for coeff, compound in zip(coeffs[len(lhs_compounds):], rhs.split('+')):
        rhs_result.append(f"{coeff if coeff != 1 else ''}{compound.strip()}")

    return " + ".join(lhs_result) + " -> " + " + ".join(rhs_result)

# ---------------- MAIN PROGRAM ---------------- #

print("Enter the unbalanced chemical equation (use '->' for reaction):")
equation = input().strip()

balanced_equation = balance_chemical_equation(equation)

print("\nBalanced Equation:")
print(balanced_equation)
