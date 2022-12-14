import sys, os, time
item = ""

def printList():
  print("\n\nTo do list:\n")
  for item in toDoList:
    print(item)
    print()

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
option = ""
while option != 4:
  option = int(input("What do you want to do?\n1. Add a task;\n2.Remove a task;\n3.Show Agenda\n4.Exit.\n"))

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
    print ("chose a right option")
    time.sleep(3)
    os.system("clear")

closing = "Closing agenda..."
for char in closing:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(0.1)
time.sleep(5)
os.system("clear")
