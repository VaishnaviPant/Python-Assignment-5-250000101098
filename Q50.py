import os

filename = "temporary.txt"

file = open(filename, "w+", encoding="utf-8")
file.write("This text was written to the file.")
file.seek(0)

print("File contents:")
print(file.read())

file.close()
print("File closed:", file.closed)

os.remove(filename)
print("File deleted.")