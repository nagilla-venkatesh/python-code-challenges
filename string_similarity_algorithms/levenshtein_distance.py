def levenshtein_distance(s, t):
    """Calculate the Levenshtein distance between two strings."""
    # Initialize matrix of zeros
    distance = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(len(s) + 1):
        distance[i][0] = i
    for j in range(len(t) + 1):
        distance[0][j] = j

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0  # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                cost = 1  # Otherwise the cost of substitution is 1
            distance[i][j] = min(
                distance[i - 1][j] + 1,  # Cost of deletions
                distance[i][j - 1] + 1,  # Cost of insertions
                distance[i - 1][j - 1] + cost,
            )  # Cost of substitutions

    return distance[len(s)][len(t)]


print(levenshtein_distance("winkler", "welfare"))
