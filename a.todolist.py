# DOCUMENTATION:
# This program adds,views,removes the tasks and also performs these functions in todolist.txt file.
# This program also saves the data (using w)in the file and when it is rerun, it can access the data stored in todolist.txt(using r)
# It is capable to save multiple data as well as single data
#CONCEPT USED : os module, wrapper(isp), time module(isp), encapulation, exception handelling, nested loop
#PROBLEM FACED: some silly mistakes regarding file name, used append instead of extend, pop index, remove element
import os
import time

def addtime(func):
   def wrapper(*args):
      func(*args)
      time.sleep(3)
   return wrapper

def add_single(my_list):
   e=input("Enter the task you want to add :")
   my_list.append(e)

def add_multiple(my_list):
    while True:
        input_task=input("Enter the tasks to be added (seperated by commas):")
        if "," in input_task:
            multiple_value_list=input_task.split(",")
            list_extended=[i.strip() for i in multiple_value_list]#i.strip removes spaces before word
            my_list.extend(list_extended)
            break
        else:
            print("use comma to separate your task")

@addtime
def view(my_list):
    print("These are the things you need to do:")
    for i in my_list:
       print(i)

def Remove(my_list):
    p=True
    while p:
            if not my_list:
             print("No task available")
             p=False
             break
            else:
             for i,j in enumerate(my_list,start=1):
              print(f"{i} {j}")
             b=int(input("enter the number of task you want to remove :"))

             if x>=b>0:
              my_list.pop(b-1)
              p=False
              break
             else:
                  print(f"Enter number between 1 - {x}")

#used before quiting
def save_task(my_list,filename=r"D:\programs\vs code python\projects\todolist\todolist1.txt"):#creates the file and makes the changes to the file according to the function
   a=os.path.join(r"D:\programs\vs code python\projects\todolist\todolist1.txt",filename)
   with open(a,"w") as file:
      for i in my_list:
         file.write(f"{i}"+"\n")

def load_previous_task(filename=r"D:\programs\vs code python\projects\todolist\todolist1.txt"):#This allows the program to start with the previously saved tasks and if no previous task returns empty my_list
   my_list=[]
   try:
    b=os.path.join(r"D:\programs\vs code python\projects\todolist\todolist1.txt",filename)
    with open(b,"r") as file:
        for text in file:
            my_list.append(text.strip())
   except FileNotFoundError:
    pass
   return my_list
   


my_list=load_previous_task()
x=len(my_list)
print("\nTODO my_list:")

while True:
    try:
        input_number=int(input('''\nWhat do you want to do?
1. Add multiple tasks to the list
2. Add single task to list
3. View the list
4. Remove something from list
5. Clear your list
6. Quit and save
='''))
        if input_number==1:
           add_multiple(my_list)
           print("Successfully Added")

        elif input_number==2:
           add_single(my_list)
           
        elif input_number==3:
           view(my_list)

        elif input_number==4:
           Remove(my_list)
           print("Successfully Removed")

        elif input_number==5:
           my_list.clear()
           print("All task cleared")

        elif input_number==6:
            save_task(my_list)
            break
        
        else:
           print(f"Enter number between 1 - 4")

    except ValueError:
        print("enter only number")

print("Do complete you work")
