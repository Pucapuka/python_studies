import sys, os, time
item = ""
def printList():
  print("\n\nTo do list:\n")
  for item in toDoList:
    print(item)

def addToList():
  item = input("What activity to add?\n")
  toDoList.append(item)

def removeFromList():
  item = input("What activity to remove?\n")
  if item in toDoList:
    toDoList.remove(item)
  else:
    print(f'The activity "{item}" isn\'t in the list.')
    
#------------MAIN FUNCTION------------------------------
toDoList = []
repeat = ""
option = int(input("What do you want to do?\n1. add a task;\n2.Remove a task;\n3.Exit.\n"))
while option != 3:
  if option == 1:
    while repeat != "no":
      addToList()
      repeat = input("Press any key to continue or type 'no' to  stop listing.")
  elif option == 2:
    while repeat != "no":
      removeFromList()
      repeat = input("Press any key to continue or type 'no' to  stop listing.")
  else:
    print ("chose a right option")
    time.sleep(3)
    os.system("clear")
    option = int(input("What do you want to do?\n1. add a task;\n2.Remove a task;\n3.Exit.\n"))

printList()

closing = "Closing agenda..."
for char in closing:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(0.1)
time.sleep(5)
os.system("clear")
