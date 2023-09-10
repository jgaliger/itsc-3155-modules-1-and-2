word = input("Please enter a random string: ")

string_placeholder = ""

for var in reversed(word):
    string_placeholder += var

# Print the reversed string
print("Reverse: " + string_placeholder)