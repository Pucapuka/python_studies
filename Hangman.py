import random

wordList = ("change", "merge", "foreign", "country")
chosenWord = random.choice(wordList)
repeat =[]
chances = 6
booleankey = True

print ("\033[34mHANGMAN. Guess the secret word letter by letter. You have 6 chances!")

while True:
  if booleankey == False:
      break
  else:
    chosenLetter = input("\033[33mType a letter: \033[32m".lower())
    if chosenLetter not in repeat:
        repeat.append(chosenLetter)
        if chosenLetter in chosenWord:
            print("\033[32mYou found one letter!")
            booleankey = False
            for i in chosenWord:
                if i in repeat:
                    print(f'{i} ', end="")
                else:
                    print("_ ", end="")
                    booleankey = True
            print()
        else:
            print("\033[31mThis letter isn't in the word!")
            chances -= 1
    else:
        print("\033[35mYou already typed this letter.")
    
    
    if chances<=0:
        print("\033[31mYou got no more chances! Your man is dead!")
        break

if booleankey == False:
    print(f"\033[32mCongratulations! You saved the man! Answer: {chosenWord}")
print ("\033[31mGAME OVER!")
