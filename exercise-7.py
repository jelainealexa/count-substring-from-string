# Return the count of a given substring from a string

# Count the substrings in the string
def substring_count(string, substring):
    return string.count(substring)

# Given strings
string_1 = "I have 7 cats. The cat is on the mat. I love cats"
string_2 = "I love chocolate. My favorite ice cream flavor is chocolate. Chocolate, chocolate, chocolate."

# Count the substrings
count_substring_1 = substring_count(string_1, "cats")
count_substring_2 = substring_count(string_2, "chocolate")

# Print the results
print(f"Cats appeared {count_substring_1} times")
print(f"Chocolate appeared {count_substring_2} times")