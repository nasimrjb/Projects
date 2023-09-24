import os
file = open('short.txt')
x = file.read()

print(os.getcwd())

# Define the target directory you want to change to
new_directory = r"D:\OneDrive\Studies\Projects\Projects"

# Change the current working directory to the new directory
os.chdir(new_directory)

# Verify the new current working directory
print(os.getcwd())
