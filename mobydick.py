#Author: Saidhbh Foley
# Counts the occurences of the letter in in moby-dick.txt

f = open("moby-dick.txt", "r")
data = f.read()
occurrences = data.count("e")
print('Number of occurences of the letter e is:', occurrences)

# References: https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/