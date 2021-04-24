"""
8 minutes of video "Python Tutorial- Calling External Commands Using the Subprocess Module"
was watched and noted in this file
I do not think "-la" is a valid command in windows cmd
"""

import subprocess

subprocess.run('python -m venv test_env', shell=True)

#shell = True is required in windows
subprocess.run('dir', shell=True)

#To run more than one command, pass the commands in a list
subprocess.run(['dir', '-la'], shell=True)

process1 = subprocess.run(['dir', '-la'], shell=True)

#to print out the error in comands execution
print(process1.stderr)

#returns the commands passed as argumnets
print(process1.args)

#returns the number of errors occured
print(process1.returncode)

#returns the ouput of external command that we run
print(process1.stdout)
#This will return None, to capture the output use 'capture_output=True'

print('-'*20, '\n'*2)
process1 = subprocess.run(['dir', '-la'], shell=True, capture_output=True)
print(process1.stdout)

print('-'*20, '\n'*2)
#This will convert the output into formatted string
print(process1.stdout.decode())
#Same output will be seen if we use 'text=True' as argument in "subprocess.run(-,-, text=True)"
print('\n'*2)

#to print out the error in comands execution
print(process1.stderr)








