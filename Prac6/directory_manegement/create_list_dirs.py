# Create nested directories
import os

os.makedirs("project/data/results", exist_ok=True)
print("Nested directories created.")

#List files and folders
import os

print("Items in current directory:")
for item in os.listdir("."):
    print("-", item)

# Find files by extension (.txt)
import os

print("TXT files:")
for file in os.listdir("."):
    if file.endswith(".txt"):
        print(file)