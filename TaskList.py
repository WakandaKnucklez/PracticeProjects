from datetime import datetime
import json
import sys

data_file = "TaskData.json"
def load_data():
    try:
        with open(data_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data():
    with open(data_file,"w") as f:
        return json.dump(tasks, f, indent=4)

tasks = load_data()

while True:
    
    desc = tasks["task"]["description"]
    new_task = input("What task do you want to add today (delete to delete/ edit to edit): ").lower()


    if new_task != "delete" and new_task != "edit" and new_task != "":
        task_status = input("Enter task status (not done/ working/ done): ").lower()
        if task_status != "not done" and task_status != "working" and task_status != "done":
            while True:
                print("incorrect status operative")
                task_status = input("Enter task status (not done/ working/ done): ").lower()
                if task_status == "not done":
                    break
                elif task_status == "working":
                    break
                elif task_status == "done":
                    break
        elif task_status == "not done":
            desc[new_task] = task_status
            tasks["AtUpdated"] = datetime.now().strftime("%m/%d/%y %H:%M")
        elif task_status == "working":
            desc[new_task] = task_status
            tasks["AtUpdated"] = datetime.now().strftime("%m/%d/%y %H:%M")
        elif task_status == "done":
            desc[new_task] = task_status
            tasks["AtUpdated"] = datetime.now().strftime("%m/%d/%y %H:%M")


    if new_task == "edit":
        edit_task = input("What task do you want to edit (status edit to edit status only): ").lower()
        if edit_task in desc:
            new_text = input("New task: ").lower()
            new_status = input("Enter task status (not done/ working/ done): ").lower()

            if new_status != "not done" and new_status != "working" and new_status != "done":
                while True:
                    print("incorrect status operative")
                    new_status = input("Enter task status (not done/ working/ done): ").lower()
                    if new_status == "not done":
                        break
                    elif new_status == "working":
                        break
                    elif new_status == "done":
                        break

            del desc[edit_task]
            desc[new_text] = new_status
            tasks["AtUpdated"] = datetime.now().strftime("%m/%d/%y %H:%M")
            save_data()
        
        elif edit_task not in desc:
            while True:
                print("task not in list!")
                edit_task = input("What task do you want to edit (status edit to edit status only): ").lower()

                if edit_task in desc:
                            new_text = input("New task: ").lower()
                            new_status = input("Enter task status (not done/ working/ done): ").lower()

                            if new_status != "not done" and new_status != "working" and new_status != "done":
                                while True:
                                    print("incorrect status operative")
                                    new_status = input("Enter task status (not done/ working/ done): ").lower()
                                    if new_status == "not done":
                                        break
                                    elif new_status == "working":
                                        break
                                    elif new_status == "done":
                                        break

                            del desc[edit_task]
                            desc[new_text] = new_status
                            tasks["AtUpdated"] = datetime.now().strftime("%m/%d/%y %H:%M")
                            save_data()
                            break

        elif edit_task == "status edit":
            change_status = input("Which task do you want to change status: ").lower()
            
            if change_status in desc:
                desc[change_status] = None
                task_status = input("Enter task status (not done/ working/ done): ").lower()
                desc[change_status] = task_status
                if task_status != "not done" and task_status != "working" and task_status != "done":
                    while True:
                        print("incorrect status operative")
                        task_status = input("Enter task status (not done/ working/ done): ").lower()
                        if task_status == "not done":
                            break
                        elif task_status == "working":
                            break
                        elif task_status == "done":
                            break
            while change_status not in desc:
                print("Operative not in list!")
                change_status = input("Which task do you want to change status: ").lower()
                if change_status in desc:
                    desc[change_status] = None
                    task_status = input("Enter task status (not done/ working/ done): ").lower()
                    desc[change_status] = task_status
                    if task_status != "not done" and task_status != "working" and task_status != "done":
                        while True:
                            print("incorrect status operative")
                            task_status = input("Enter task status (not done/ working/ done): ").lower()
                            if task_status == "not done":
                                break
                            elif task_status == "working":
                                break
                            elif task_status == "done":
                                break
                break



    if new_task == "delete":
        delete_task = input("Wich task do you want to delete (type dont delete to go back): ").lower()
        if delete_task == "dont delete":
            continue
        elif delete_task in desc:
            del desc[delete_task]
            print("Item Deleted!")
            save_data()
        elif delete_task not in desc:
            while True:
                print("Item not deleted, Item not in list")
                delete_task = input("Wich task do you want to delete (type dont delete to go back): ").lower()
                if delete_task in desc:
                    del desc[delete_task]
                    print("Item Deleted!")
                    save_data()
                    break
                if delete_task == "dont delete":
                    break 
            if delete_task == "dont delete":
                continue
                

    if new_task == "":
        pass

    asked = input("Do you want to add anything else (n/y): ").lower()

    if asked == 'n':
        tasks["AtUpdated"] = datetime.now().strftime("%m/%d/%y %H:%M")
        print("Youre tasks are:")
        for key, value in desc.items():
            print(f"Youre tasks: {key} : {value}")
        print(f"List Update at: {tasks["AtUpdated"]}")
        save_data()
        break
    elif asked == 'y':
        continue

    while asked != "y" and asked != "n":
        print("incorrect operative, please selecet y/n")
        asked = input("Do you want to add anything else (n/y): ").lower()
        if asked == 'y':
            break
        if asked == 'n':
            tasks["AtUpdated"] = datetime.now().strftime("%m/%d/%y %H:%M")
            print("Youre tasks are:")
            for key, value in desc.items():
                print(f"Youre tasks: {key} : {value}")
            print(f"List Update at: {tasks["AtUpdated"]}")
            save_data()
            sys.exit()
            break