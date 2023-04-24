def jaro_winkler(s, t):
    """Calculate the Jaro Winkler distance between two strings."""
    # Initialize the Jaro Winkler distance
    jaro_winkler_distance = 0

    # Calculate the Jaro distance
    # Initialize the Jaro distance
    jaro_distance = 0

    # Find the number of matching characters
    matches = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            matches += 1

    # Find the number of transpositions
    transpositions = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i] in t:
                transpositions += 1

    # Calculate the Jaro distance
    jaro_distance = (1/3) * (matches/len(s) + matches/len(t) + (matches-transpositions)/matches)

    # Calculate the Jaro Winkler distance
    # Find the number of matching characters at the beginning
    prefix_length = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            prefix_length += 1
        else:
            break

    # Calculate the Jaro Winkler distance
    jaro_winkler_distance = jaro_distance + 0.1 * prefix_length * (1 - jaro_distance)

    return jaro_winkler_distance

print(jaro_winkler("monica", "monika"))