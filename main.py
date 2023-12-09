print("     TASK PRIORITY SCHEDULER      \n")

while(True):
    file = open("TASK.csv","r")

    task_data = file.readlines()

    if(len(task_data) == 0):
        print("NO TASK FOUND .... ....")
    else:
        counter = 1
        check = False

        print("\nHight Priority Tasks : \n")
        for i in task_data:
            task = i.split(",")
            if(task[0] == "High"):
                check = True
                print(counter , "   " , task[1])
                counter +=1
        
        if(check == False):
            print("No High Priority Task Found\n")

        check = False

        print("Medium Priority Tasks : \n")
        for i in task_data:
            task = i.split(",")
            if(task[0] == "Medium"):
                check = True
                print(counter , "   " , task[1])
                counter +=1

        
        if(check == False):
            print("No Medium Priority Task Found\n")
        
        check = False

        print("\nLow Priority Tasks : \n")
        for i in task_data:
            task = i.split(",")
            if(task[0] == "Low"):
                check = True
                print(counter , "   " , task[1])
                counter +=1
        
        if(check == False):
            print("No Low Priority Task Found\n")

        print("\nOptions :-")

        print("\n1) Add Task")
        print("2) Remove Task")
        print("0) Exit")
        
        optioninput = int(input("\nEnter Choice : "))

        if(optioninput == 1):
            print("\nAdd Task")

            file = open("TASK.csv","a")

            task_detail = input("\nEnter Task Description : ")

            task_priority = input("Enter Task Priority (High,Medium,Low) (check spellings please) : ")

            file.write(task_priority + "," + task_detail + "\n")
            file.close()

            print("\nTask Added Successfully")
    
        elif(optioninput == 2):

            print("\nRemove Task")

            task_index = int(input("\nEnter Task Number From Above : "))
            if(task_index > len(task_data)):
                print("\nPLease Enter Valid Task Index")
            else:
                task_data.pop(task_index-1)
                file = open("TASK.csv","w")
                file.writelines(task_data)
                print("\nTask Removed Successfully")

            
        elif(optioninput == 0):
            print("\nExited")
            break
        else:
            print("\nInvalid Input , Check Options And Re Enter Choice")
        