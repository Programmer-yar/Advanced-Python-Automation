import sys

"""
- involves using "argv" of sys module
- "sys.argv" contains a list, first item is the name of script file
  remaining items contain the args passed to the script
- To run this script type the following in the command line
  python "sys argv test.py" somename
""" 
print(sys.argv, '\n')
print("Your name is : ", sys.argv[1])
    
