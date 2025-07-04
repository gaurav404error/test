# Your to-do items
todo_list = [
    "Drink water",
    "Finish Python assignment",
    "Go for a walk",
    "Call mom"
]

# Time gap between notifications (in seconds)
time_gap = 10  # you can change it to 3600 (1 hour) or any value

for task in todo_list:
    notification.notify(
        title="📝 To-Do Reminder",
        message=task,
        timeout=10  # Notification stays for 10 seconds
    )
    time.sleep(time_gap)
    exit()

    print ("i am good/nand you are good")
    
    