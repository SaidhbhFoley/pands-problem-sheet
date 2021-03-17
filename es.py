# Program that reads in a text file
# Outputs the number of e's it contains.
# Author: Saidhbh

filename = input("Enter file name: ")
l=input("Enter letter to be searched:")
k = 0
 
with open(filename, 'r') as f:
    for line in f:
        words = line.split()
# splits line to get list of words
        for i in words:
            for letter in i:
                if(letter==l):
                    k=k+1
print("Occurrences of the letter:")
print(k)

# source: https://www.sanfoundry.com/python-program-read-file-counts-number/
# moby dick text source: https://gist.github.com/StevenClontz/4445774