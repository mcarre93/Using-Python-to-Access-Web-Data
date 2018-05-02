# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and
# numbers. You will extract all the numbers in the file and compute the sum
# of the numbers.
# Handling The Data
# The basic outline of this problem is to read the file, look for integers using
# the re.findall(), looking for a regular expression of '[0-9]+' and then
# converting the extracted strings to integers and summing up the integers.
import re
total_list = []
name = input("Enter file:")
handle = open(name)
# Extract numbers into list from file
for line in handle:
    num_list = re.findall('[0-9]+', line)
    total_list.append(num_list)
#print(total_list)
sum = 0
for list in total_list:
    for number in list:
        sum = sum + int(number)

print(sum)
