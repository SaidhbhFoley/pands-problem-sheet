# Program that reads in a text file
# Outputs the number of e's it contains.
# Author: Saidhbh

filename = input("Enter file name: ")
l=input("Enter letter to be searched:")
k = 0
 
with open(filename, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter==l):
                    k=k+1
print("Occurrences of the letter:")
print(k)

# source: https://www.sanfoundry.com/python-program-read-file-counts-number/