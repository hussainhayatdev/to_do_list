while True:
    try:
        with open("tasks.txt","r") as file:
            tasks = file.readlines()
        tasks =[task.strip() for task in tasks]
    except FileNotFoundError:
        tasks=[]
    print("--Your tasks--")
    for i,task in enumerate(tasks):
        print(f"{i+1}.{task}")
    task = input("Enter a new task(enter if no):")
    if task:
        tasks.append(task)
        for i,task in enumerate(tasks):
            print(f"{i+1}.{task}")
    remove = input("Remove a task by number(enter if no):")
    if remove:
        length = len(tasks)
        while True:
            try:
                remove= int(remove)
                while remove>length or remove<1:
                    print("This task doesnt exist!")
                    remove = int(input("Enter no. of task to remove:"))
                break
            except ValueError:
                remove=input("Only enter a number:")
    tasks.pop(remove-1)
    for i,task in enumerate(tasks):
        print(f"{i+1}.{task}" )
    with open("tasks.txt","w") as file:
        file.writelines(task+"\n" for task in tasks)
    choice = input("would you like to run the program again(yes/no):").lower()
    while choice not in ["yes","no"]:
        choice=input("Only choose yes or no:").lower()
    if choice=="yes":
        pass
    else:
        break