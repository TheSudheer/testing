# Welcome message
print("Welcome to the Love Calculator.")

# Input names from the user
name_1 = input("What is your name?  \n")
name_2 = input("What is their name?  \n")

# Combine names and convert to lowercase for case-insensitive comparison
combined_string = name_1 + name_2
lower_case_string = combined_string.lower()

# Print the lowercase combined string for debugging purposes
print(lower_case_string)

# Count the occurrences of each letter in the combined string
# Calculate the 'TRUE' and 'LOVE' scores
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e

# Combine 'TRUE' and 'LOVE' scores to get the love score
love_score = int(str(true) + str(love))

# Check different love score ranges and provide appropriate messages
if (love_score > 10) or (love_score < 90):
    print(f"Your love score is {love_score}, you go together like Coke and Mentos.")
elif (love_score > 40) and (love_score < 50):
    print(f"Your love score is {love_score}, you go together like chilaka gorinka.")
else:
    print(f"Your love score is {love_score}")











