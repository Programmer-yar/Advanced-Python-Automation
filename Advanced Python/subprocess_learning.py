import subprocess

output = subprocess.run("dir", capture_output=True, shell=True, text=True)
isinstance(output, str)

#print(output)
#subprocess.run(['cmd', '/c', "dir"])
