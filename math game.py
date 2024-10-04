#this is a game in which there's gonna be generated a random number to operate with the chosen number family:

#Importing the random module:
import random

#organizing the functions that will execute the operations:
def addition(Rsm, mainNumber):
  print(Rsm,"+",int(mainNumber))
  sum = Rsm + mainNumber
  return sum
  
def subtraction(Rs, mainNumber):
  print(int(Rs), "-", int(mainNumber))
  sub = Rs - mainNumber
  return sub
  
def multiplication(Rsm, mainNumber):
  print(int(Rsm), "x", int(mainNumber))
  mult = Rsm * mainNumber
  return mult
  
def division(Rd, mainNumber):
  #generating a random number that is divisible by the main number: 
  
  print(int(Rd), ":", int(mainNumber))
  div = Rd / mainNumber
  return div

#Let the game begin:
print("\033[33m Math game")
operation = int(input("\n1. Addition;\n2. Subtraction;\n3. Multiplication;\n4. Division.\nChoose the operation you want to be tested: \033[32m"))
while operation not in range (1,5):
  operation = int(input("\033[33m\n1. Addition;\n2. Subtraction;\n3. Multiplication;\n4. Division.\nChoose an available operation: \033[32m"))

mainNumber = int(input("\033[33mName the number you want to be tested on (between 0 and 100): \033[32m"))

while mainNumber not in range (0,101):
  mainNumber = int(input("\033[33mChoose a number between 0 and 100!"))

#Chances and points:
counter = 0;
point = 0;

   
if operation == 1:
  while counter in range(0,10):
    #Variable to store the random numbers
    Rsm = random.randint(0,100)

    sum = addition(Rsm, mainNumber)
    answer = int(input("\033[33mWhat's the right answer? \033[32m"))
    if answer == sum:
      print("\033[33mCorrect!")
      counter += 1
      point += 1
    else:
      print("\033[33mWrong!")
      counter += 1     
        
elif operation == 2:
  while counter in range(0,10):
    #variable to store the random numbers
    Rs = random.randint(mainNumber,100)

    sub = subtraction(Rs, mainNumber)
    answer = int(input("\033[33mWhat's the right answer? \033[32m"))
    if answer == sub:
      print("\033[33mCorrect!")
      counter += 1
      point += 1
    else:
      print("\033[33mWrong!")
      counter += 1
        
elif operation == 3:
  while counter in range(0,10):
    #Variable to store the random numbers
    Rsm = random.randint(0,100)
    mult = multiplication(Rsm, mainNumber)
    answer = int(input("\033[33mWhat's the right answer? \033[32m"))
    if answer == mult:
      print("\033[33mCorrect!")
      counter += 1
      point += 1
    else:
      print("\033[33mWrong!")
      counter += 1  

elif operation == 4:
  while counter in range(0,10):
    #variable to store the random numbers
    Rd = random.randint(mainNumber,100)

    div = division(Rd, mainNumber)
    answer = int(input("\033[33mWhat's the right answer? \033[32m"))
    if answer == div:
      print("\033[33mCorrect!")
      counter += 1
      point += 1
    else:
      print("\033[33mWrong!")
      counter += 1
  
print(f'GAME OVER!!!\nYour Score:\033[32m{point}')
