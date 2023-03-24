#=====importing libraries===========
'''This is the section where you will import libraries'''
import re
from textwrap import fill


# Variables required at multiple points
# Text split patterns (using the re module)
task_split_pattern = "\n+"
sub_split_pattern = ",\s*"

# Task attributes for formatted output
attributes = ["Task:", "Assigned to:", "Task description:", "Date assigned",
                "Due date:", "Task complete"]

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
# Read in user names and passwords
# Let us hard-code the filename for re-use at various points in the program
# and ease of changing later.
user_file = "user.txt"

# Let us repeat this for the tasks file.
tasks_file = "tasks.txt"

#   Let us access the file `user.txt` and read in as a string, closing the 
# file automatically by using a `with` statement.
with open(user_file, "r") as f:
    users_import = f.read()
# Let us split this into a list of user-password pairs
user_pairs = [item.split(", ") for item in users_import.split('\n')]

# Let us now split the pairs and store all pairs in a dictionary object
user_logins = {pair[0] : pair[1] for pair in user_pairs}

# Ask for user name and password.
# Ask for username first, and check that it is a valid username.
while True:
    entered_username = input("Please enter your username: ")
    # Confirm that a valid username has been entered
    if entered_username not in user_logins:
        # Report username not found, and delete from memory to avoid confusion.
        print("User not recognised. Please try again")
        del(entered_username)
        continue
    # Leave loop if username is validated
    break
    
while True:
    entered_password = input("Please enter your password: ")
    
    # Check password, remain in loop until the correct password is provided.
    if entered_password != user_logins[entered_username]:
        print("Wrong password. Please try again")
        continue
    # Leave loop if password is correct
    break

# Print blank lines with a horizontal line in between for clarity

print()
print("─" * 54)
print()
               
# Beginning of main program loop
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user (admin only)
a - Adding a task
va - View all tasks
vm - view my task
st - View basic statistics (admin only)
e - Exit
: ''').lower()

    if menu == 'r':
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
            
        # Let us print out a line between spaces for clarity.
        print()
        print("─" * 54)
        print()    
        
            
        # Let us fulfil the requirement for user "admin" to be the only user 
        # able to do this.
        if entered_username != "admin":
            # Notify user that they do not have the credentials to use this 
            # option.
            print ("This task may only be performed by user 'admin'")
            
            # Print blank lines with a horizontal line in between for clarity
            print()
            print("─" * 54)
            print()
            
            # Return to menu loop
            continue
        
        # Read in the details as specified from user "admin"
        new_username = input("Please enter a new username: ")
        new_password = input(f"Please enter a new password for {new_username}: ")
        confirm_password = input("Please confirm the password: ")
        
        # If passwords do not match, print message, remove entries and 
        # return to menu.
        if new_password != confirm_password:
            # Print message
            print("Passwords do not match. User {new_username} NOT added.")
            
            # Delete newly-inputted variables:
            del(new_username); del(new_password); del(confirm_password)
            
            # Return to menu
            continue
        
        # Add user and password to file.
        with open(user_file, "a") as f:
            f.write(f"\n{new_username}, {new_password}")
        
        # Confirm adding.
        print(f"New user {new_username} added OK.")
        
        # Print blank lines with a horizontal line in between for clarity
        print()
        print("─" * 54)
        print()

    elif menu == 'a':
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
            
        # Let us print out a line between spaces for clarity before requesting details.
        print()
        print("─" * 54)
        print() 
            
        # Read in te username of the person whom the task is assigned to
        intended_user = input("Please enter a user name to assign the task to: ")
        
        # Read in the title of the task
        task_title = input(
            "Please enter a the task title (title only at this step): ")
        
        # Read in the description of the task
        description = input("Please enter a the task description: ")
        
        # Read in the due date
        due_date = input("Please enter a due date, format e.g. 10 Oct 2019: ")
        
        # Confirm Current date
        current_date = input(
            "Please confirm the current date, format format e.g. 10 Oct 2019: ")
        
        # Form list to format into task string at next step
        new_task = [intended_user, task_title, description, due_date, 
                    current_date, "No"]
        
        # Generate task string
        task_string = "\n" + ", ".join(new_task)
        
        # Write (append mode) tasks to file.
        with open(tasks_file, "a") as f:
            f.write(task_string)
            
        # Confirm task added OK to user
        print("Task added OK")
            
        # Print blank lines with a horizontal line in between for clarity
        print()
        print("─" * 54)
        print()
        
    elif menu == 'va':
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

        #Let us instantiate a list of attributes of a task:
        attributes = ["Assigned to:", "Task:", "Task description:", "Date assigned",
                "Due date:", "Task complete"]

        # Now let us read in the task file, first in a string variable `tasks_import`.
        with open(tasks_file, "r") as f:
            tasks_import = f.read()
            
        #   Now let us create a list of strings, each of which contains the details 
        # of a task.
        #   This will be done by splitting at new line characters, the use of 
        # re.split enables blank lines to be ignored safely.
        task_split_pattern = "\n+"
        task_list = re.split(task_split_pattern,tasks_import)

        #   Now let us define a pattern to split within the string.
        sub_split_pattern = ",\s*"

        # Now let us iterate over the list of single-task strings.
        for item in task_list:
            sub_list = re.split(sub_split_pattern, item)
            
            # Start by printing a horizontal line above the task details for clarity.
            print()
            print("─" * 54)
            print()
            
            # Print the details other than description, then the description.
            for i in range(len(sub_list)):
                if i == 2:
                    continue
                print (attributes[i].ljust(19), sub_list[i])
            # Let us use different formatting for the description, as per the 
            # specification.
            else:
                print(attributes[2])
                print(fill(sub_list[2], initial_indent = " "))
        else:
            # To run after the last task, prints blank lines with a horizontal line in between 
            # the last task.
            print()
            print("─" * 54)
            print()

    elif menu == 'vm':
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''
            
        # Let us first read in all the tasks. As they are in plain text, it will be possible to detect if 
        # there are no tasks and report accordingly. 
        with open(tasks_file, "r") as f:
            tasks_import = f.read()
            
        if entered_username not in tasks_import:
            
            # Print line at start for clarity, and also consistency with other sections.
            print()
            print("─" * 54)
            print()
            
            # Notify that no tasks are assigned if this point is reached.
            print("No tasks assigned to this user")
        
            # Print line at end for clarity, and also consistency with other sections.
            print()
            print("─" * 54)
            print()
            
            # Return to main loop
            continue
        
        #   Now let us create a list of strings, each of which contains the details 
        # of a task.
        #   This will be done by splitting at new line characters, the use of 
        # re.split enables blank lines to be ignored safely.
        task_split_pattern = "\n+"
        task_list = re.split(task_split_pattern,tasks_import)
        
        # Let us perform a second test, as the username should be the first word in each line
        users_assigned = [word.split(', ')[0] for word in task_list]
        
        if entered_username not in users_assigned:
            print("No tasks assigned to this user")
        
            # Print line at end for clarity, and also consistency with other sections.
            print()
            print("─" * 54)
            print()
            
            # Return to main loop
            continue

        #   Now let us define a pattern to split within the string.
        sub_split_pattern = ",\s*"

        # Now let us iterate over the list of single-task strings.
        for item in task_list:
            sub_list = re.split(sub_split_pattern, item)
            
            # Skip over items not for user:
            if sub_list[0] != entered_username:
                continue
            
            # Start by printing a line above the task details for clarity, followed by a blank line
            print()
            print("─" * 54)
            print()
            
            # Print the details other than description, then the description.
            for i in range(len(sub_list)):
                if i == 2:
                    continue
                print (attributes[i].ljust(19), sub_list[i])
            # Let us use different formatting for the description, as per the 
            # specification.
            else:
                print(attributes[2])
                print(fill(sub_list[2], initial_indent = " "))
        else:
            # To run after the last task, prints an extra line for clarity after 
            # the last task.
            print("─" * 54)
    
    elif menu == 'st':
        # Additional section to print number of tasks and users
        # Print blank line then horizontal line at start for clarity, and also consistency 
        # with other program sections.
        print()
        print("─" * 54)
    
        if entered_username != "admin":
            # Notify user that they do not have the credentials to use this 
            # option.
            print ("This task may only be performed by user 'admin'")
            
            # Print horizontal line for clarity, then blank line
            print("─" * 54)
            print()
            
            # Return to menu loop
            continue
    
        # Let us obtain the number of tasks, by reading in the task file, splitting 
        # to task strings and printing the number of task strings to screen:
        with open(tasks_file, "r") as f:
            tasks_import = f.read()
        task_list = re.split(task_split_pattern,tasks_import)
        print("The total number of tasks is", len(task_list))
        
        # Let us repeat this for the number of users, splitting by line and printing 
        # the number of users to screen.
        with open(user_file, "r") as f:
            users_import = f.read()
        # Let us split this into a list of user-password pairs
        user_pairs = [item.split(", ") for item in users_import.split('\n')]
        # Let us print a count to screen:
        print("The number of users registered is", len(user_pairs))
        
        # Print line at end for clarity, and also consistency with other sections.
        print("─" * 54)
        print()
    
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")