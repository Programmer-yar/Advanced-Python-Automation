import subprocess

"""
- python will not throw an exception if an external command fails
- python will throw an exception if "check=True" is included as kwarg in
  "subprocess.run()"
"""
p1 = subprocess.run(['dir', 'not_there'], capture_output=True, text=True,
                    shell=True)
print("Output: ", p1.stdout)
print("Error: ", p1.stderr)
print("Error Code: ", p1.returncode)

#"subprocess.DEVNULL" can also be used to ignore errors
#or redirecting standard error to DEVNULL
p2 = subprocess.run(['dir', 'no folder'], stderr=subprocess.DEVNULL, shell=True)
print(p2.stderr)

#while running windows cmd commands include "shell=True" in
#"subprocess.run" as kwarg
with open('output.txt', 'w') as f:
    subprocess.run('dir', stdout=f, text=True, shell=True)
