import random

wordList = ("change", "merge", "foreign", "country")
repeat = []
chosenWord = random.choice(wordList)
chances = 6


while True:
    chosenLetter = input("Type a letter: ")
    if chosenLetter not in repeat:
        repeat.append(chosenLetter)
        if chosenLetter in chosenWord:
            print("You found one letter!")
            False
            for i in chosenWord:
                if i in repeat:
                    print(i, end="")
                else:
                    print("_", end="")
                    True
            print()
        else:
            print("This letter isn't in the word!")
            chances -= 1
    else:
        print("You already typed this letter.")
    
    
    if chances<=0:
        print("You got no more chances! Your man is dead!")
        break
print ("GAME OVER!")
    
    
