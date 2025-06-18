def percentage_match(seq1, seq2):
    # Find the length of the shorter sequence to avoid index errors
    length = min(len(seq1), len(seq2))
    if length == 0:
        return 0  # Avoid division by zero

    matches = 0
    for i in range(length):
        if seq1[i] == seq2[i]:
            matches += 1

    # Calculate percentage of matching elements
    percentage = (matches / length) * 100
    return percentage

# Example usage:
seq1 = "ABCD"
seq2 = "ABCF"
print(f"Percentage match: {percentage_match(seq1, seq2)}%")  # Output: 75.0%
