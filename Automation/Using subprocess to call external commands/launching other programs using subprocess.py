import subprocess

calc_process = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
print(calc_process.poll() == None)
print(calc_process.wait())
print(calc_process.poll())
