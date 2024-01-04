# Function to get user input for the step and information
def get_user_input():
    step = input("Enter the step you just took (press Enter twice to finish):\n")
    info = input("How did you get this information (press Enter twice to finish):\n")
    return step, info


# Function to log the tool and information to a specified text file
def log_to_file(tool, step, info, file_name):
    with open(file_name, "a") as log_file:
        if tool:
            tool_name = input("What tool did you use: ")
            log_file.write(f"Tool: {tool_name}\n")
        log_file.write(f"Step: {step}\n")
        log_file.write(f"Information: {info}\n")
        log_file.write("\n")

# Main program
file_name = input("Enter the name of the file you want to edit or create (e.g., cybersecurity_log.txt): ")

# Check if the log file exists, and if not, create it
try:
    with open(file_name, "r"):
        pass
except FileNotFoundError:
    with open(file_name, "w"):
        pass

while True:
    try:
        tool_question = input("Did you use a tool for this step? (yes/no): ").lower()
        tool = tool_question == 'yes','Yes'
        step, info = get_user_input()
        log_to_file(tool, step, info, file_name)
        print(f"Log entry saved to {file_name}.")
        more = input("Do you want to add another log entry? (yes/no): ")
        if more.lower() != 'yes':
            break
    except KeyboardInterrupt:
        print("Program terminated.")
        break

# Function to get user input for the step and information
def get_user_input():
    print("Enter the step you just took (press Enter twice to finish):")
    step = []
    while True:
        line = input()
        if line == "":
            break
        step.append(line)
    step = "\n".join(step)
    
    print("How did you get this information (press Enter twice to finish):")
    info = []
    while True:
        line = input()
        if line == "":
            break
        info.append(line)
    info = "\n".join(info)

    return step, info

