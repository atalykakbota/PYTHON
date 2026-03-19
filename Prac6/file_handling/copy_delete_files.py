#1 copy

import shutil

shutil.copy("tasks.txt", "tasksbackup.txt")
print("Backup created: tasksbackup.txt")

#2 delete
import os

if os.path.exists("tasksbackup.txt"):
    os.remove("tasksbackup.txt")
    print("Backup file deleted safely.")
else:
    print("Backup file does not exist.")

