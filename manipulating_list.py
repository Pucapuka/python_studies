listOfShame = []
listTitle = ["Name", "Age", "OS"]

def organizedPrint():
  for row in listTitle:
      print(f'{row:^10}\t', end= '|')
  print()  
  for row in listOfShame:
    for i in row:
      print(f'{i:^10}\t', end = '|')   #it's more complex than the previous loop because it's a list inside another list. So I had to pick each item of "row" to print
    print()
  print()
  
while True:
  name = input("What is your name? ")
  age = input("How old are you? ")
  pref = input ("What's your Computer platform? ")
  row = [name, age, pref]
  listOfShame.append(row)
  exit = input("Exit? y/n ")
  if (exit.strip().lower()[0]=="y"):
    break

organizedPrint()
