#Prompt for a Single Task
task = input("Enter your task: ")
priority = input("priority (high/medium/low): ")
time_bound = input("Is it time_bound? (yes/no): ")

#Process the Task Based on Priority and Time Sensitivity
match priority.lower():
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"

# Modify the reminder if the task is time-bound
if time_bound.lower() == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Provide a customized reminder
print(f"Reminder: {reminder}")
        