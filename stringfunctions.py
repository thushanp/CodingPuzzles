# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character.

# Code all three

string = "hellomyname"

# insert 
new = list(string)

new.insert(4, "x")

print(new)

# replace

print(string.replace("l", "z", 1))

# remove

new.remove("l")

print(new)

del new[-1]

print(new)