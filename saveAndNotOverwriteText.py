myEvents = []

f = open("calendar.txt", 'r')
myEvents = eval(f.read())
f.close()
def coolPrint():
  print()
  for row in myEvents:
    print(f'{row[0]:^15} {row[1]:^15}')
  print()

while True:
  menu = int(input("1: Add, 2: Remove\n"))
  if menu == 1:
    event = input("What event?: ").capitalize()
    date = input("What date?: ")
    row = [event, date]
    myEvents.append(row)
    coolPrint()
  else:
    criteria = input("What event do you want to remove?:").capitalize()
    for row in myEvents:
      if criteria in row:
        myEvents.remove(row)
    coolPrint()

  f = open("calendar.txt", 'w')
  f.write(str(myEvents)) 
  f.close()
