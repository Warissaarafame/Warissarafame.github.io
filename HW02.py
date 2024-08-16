def length_of_longest_substring_k_distinct(s: str, k: int) -> tuple:
    # Your implementation here
    pass

# Example usage:
if __name__ == '__main__':
    print(length_of_longest_substring_k_distinct("eceba", 2))  # Output: (3, ["ece"])
    print(length_of_longest_substring_k_distinct("aa", 1))     # Output: (2, ["aa"])
    print(length_of_longest_substring_k_distinct("a", 2))      # Output: (1, ["a"])
    print(length_of_longest_substring_k_distinct("abcadcacacaca", 3))  # Output: (11, ["cadcacacaca"])
