'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import random

wordList = ("change", "merge", "foreign", "country")
repeat = []
chosenWord = random.choice(wordList)
chances = 6
booleankey = True

while True:
  if booleankey == False:
      break
  else:
    chosenLetter = input("Type a letter: ")
    if chosenLetter not in repeat:
        repeat.append(chosenLetter)
        if chosenLetter in chosenWord:
            print("You found one letter!")
            booleankey = False
            for i in chosenWord:
                if i in repeat:
                    print(i, end="")
                else:
                    print("_", end="")
                    booleankey = True
            print()
        else:
            print("This letter isn't in the word!")
            chances -= 1
    else:
        print("You already typed this letter.")
    
    
    if chances<=0:
        print("You got no more chances! Your man is dead!")
        break

if booleankey == False:
    print(f"Congratulations! You saved your man! Answer: {chosenWord}")
print ("GAME OVER!")
    
    
