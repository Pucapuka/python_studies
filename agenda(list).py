import sys, os, time
item = ""

def printList():
  print("\n\n\033[35mTo do list:\n")
  for item in toDoList:
    print(item)
    print()

def addToList():
  item = input("\033[34mWhat activity to add?\n")
  toDoList.append(item)

def removeFromList():
  item = input("\033[31mWhat activity to remove?\n")
  if item in toDoList:
    toDoList.remove(item)
  else:
    print(f'\033[32mThe activity "{item}" isn\'t in the list.')
    
#------------MAIN FUNCTION------------------------------
toDoList = []
option = ""
while option != 4:
  option = int(input("\033[33mWhat do you want to do?\n\033[34m1. Add a task;\n\033[31m2. Remove a task;\n\033[35m3.Show Agenda\n\033[36m4.Exit.\n"))

  if option == 1:
    addToList()
    print()
  elif option == 2:
    removeFromList()
    print()
  elif option == 3:
    printList()
    print()
  elif option != 4:
    print ("\033[31mChoose a right option!")
    time.sleep(3)
    os.system("clear")

closing = "\033[36mClosing agenda..."
for char in closing:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(0.1)
time.sleep(5)
os.system("clear")
