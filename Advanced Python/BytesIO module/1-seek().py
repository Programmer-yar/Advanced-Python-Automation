file = open("foo.txt", "r+")
print("Name of the file: ", file.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

#pointer at line 1
line = file.readline()
print(f"Read Line: {line}")

#file.seek(offset, from_what)
# 0 -> begining of file, 1 -> current, 2 -> end
#Again set the pointer to the beginning
file.seek(10,0)
line = file.readline()
print("Read Line: %s" % (line))

# Close opend file
file.close()
