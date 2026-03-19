import shutil

shutil.copy("tasks.txt", "project/tasks_copy.txt")
shutil.move("tasks.txt", "project/tasks_moved.txt")

print("tasks.txt copied and moved successfully.")
