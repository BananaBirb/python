#! /usr/bin/env python
# added shebang in the beginning to have python scripts take input
import sys

# write a function with def to generate text output in the terminal that additionally takes user input.
# for that user input, the variables name, date and study are defined and printed out.

def printout(name, date, study):
    print(name)
    print(date)
    print(study)
    print("Ein simpler Satz.")
    print("STOP!!!")
    print("Applied Bioinformatics and Biostatistics - ABI-2022-2")

# tell python from where to take input via sys.arv. sys.argv takes the arguments from the terminals
# command line, making it easy to parse arguments into the python script.
printout(sys.argv[1],sys.argv[2],sys.argv[3])