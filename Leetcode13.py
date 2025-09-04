def romanToInt(s):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0

    for c in reversed(s):

        if d[c] < prev:
            total -= d[c]
        else:
            total += d[c]
        prev = d[c]

    return total

# Example usage:
s = "MCMXCIV"
print(romanToInt(s))  # Output: 1994