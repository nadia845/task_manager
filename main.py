# Numbering using  for Loop

"""file = open("tasks.txt", "r")
tasks =file.read().split("\n")
for task in tasks:
    print(f"{tasks.index(task)+1}. {task}")"""

    # Addition using Loop
# use a loop to calculate the sum of the two numbers below
"""numbers = [10, 5, 20, 8, 15]
sum = 0
for number in numbers:
    sum += number
print(sum)"""


# print the firstname
# open the file emails.txt in READ mode
"""email_file = open("emails.txt", "r")
emails = email_file.read().split("\n")
print(emails)
# names = []

for email in emails:
    name = email.split("@")[0]
    print(name)"""
    
    # names.append(name)
    # print(name)
# print(names)

# Read and split the data using \n to get a list
# Loop over the list of emails and print a generated username foreach of them i.e username in all characters before the @


# functions
"""def register_user(name, email, password):
    # Check if user does not already exist
    # Hash user password
    # Validate inputs
    # Check if user is not a robot
    # Return response
    return "user registered successfully!"

# Calling the regiter user function
register_user("Micheal Hammond", "mickymond@yahoo.com", "1234567890")"""


# defifine a function to add a task
"""def add_task(task):
# Save task to database
task = input("What tasks do you want to perform today: ")
    # Return response
     return task"""
# add task


# Function to output task
"""def show_task():
    #  Get all tasks from database
    # Return response 
     task = input("Enter your task")
     task.append(task)
     print(tasks)
     return tasks"""



"""import add
import show
import update
import delete

add_task_response = add.add_task("sleep")
print(add_task_response)

show_task_response = show.show_task()
print(show_task_response)

update_task_response = update.update_task("sleep", "wake up")
print(update_task_response)

delete_task_response = delete.delete_task("wake up")
print(delete_task_response)"""

# from oop import chat

# chat_with_abena = chat()
# """chat_with_micheal = chat("Micheal Hammond", "Extend the portfolio deadline", "5:56 AM")
# chat_with_0248470214 = chat("The closer", "when are we ending the class?", "3:59 PM")

# print(chat_with_0248470214.open())"""
# print(chat_with_abena)

#### TKINTER ###
# from commands import save_task
# from commands import get_tasks
# task_title = input("What task are you going to do?: ")
# save_task({"title": task_title})

# for task in get_tasks():
#     print(task)


import tkinter as tk
import ui


app = tk.Tk()
app.title("Task Manager")
app.geometry("720x480")

ui.show_all_tasks_frame(app)

app.mainloop()




