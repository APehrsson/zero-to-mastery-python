#debugging

#linting
#IDEs gives you hints when coding, helping you to find wrongs in your code at a early stage
#learn to read errors. What does the message mean? 

#pdb = python debugger, built in module
import pdb
def add(num1, num2):
    pdb.set_trace()
    return num1 + num2

add(4, 'sfdgdfh')