# This is a python script to remove special characters and numbers.
from sys import argv
import re

file = open("output.txt", "w")

script, filename = argv

with open(filename,'r') as f:
    for line in f:
        for word in line.split():
            file.write(re.sub('[^a-zA-Z]', '', word)+"\n") 

f.close()
file.close()


