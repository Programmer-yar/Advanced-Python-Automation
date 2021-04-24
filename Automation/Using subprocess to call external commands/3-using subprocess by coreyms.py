import subprocess

#gives the text output of the text file
p1 = subprocess.run(['type', 'test.txt'], capture_output=True, text=True,
                    shell=True)

#takes the output of p1 and finds the given string and gives output
p2 = subprocess.run(['findstr', '-na', 'example.'], capture_output=True,
                    text=True, input=p1.stdout, shell=True)
print(p2.stdout)
