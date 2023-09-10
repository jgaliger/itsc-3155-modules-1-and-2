word = input("Please enter a random word: ")

string_placeholder =""

for var in word:
    if var.islower():
        string_placeholder += var
for var in word:
    if var.isupper():
        string_placeholder +=var

print("Refined:" + string_placeholder)