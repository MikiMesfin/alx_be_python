#Prompt for a Single Task
task = input("Enter your task: ").lower()
priority = input("priority (high/medium/low): ").lower()
time_bound = input("Is it time_bound? (yes/no): ").lower()

#Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task.")
    case "medium":
            print(f"Reminder: '{task}' is a medium priority task.")
    case "low":
        if time_bound == "no":
            print(f"Reminder: '{task}' is a low priority task.Consider completing it when you have free time.")
        else:
            print(f"Reminder: '{task}' is a low priority task.")
    case _:
        print("Invalid priority or time-bound entered. Please enter the correct input.")

        