import random

wordList = ("mudar", "imergir", "estrangeiro", "pais")
repeat = []
chosenWord = random.choice(wordList)
chances = 6
booleankey = True

print ("\033[34mJogo da forca. Adivinhe a palavra letra a letra. Você tem 6 chances!")

while True:
  if booleankey == False:
      break
  else:
    chosenLetter = input("\033[33mDigite uma letra: \033[32m".lower())
    if chosenLetter not in repeat:
        repeat.append(chosenLetter)
        if chosenLetter in chosenWord:
            print("\033[32mVoce achou uma letra!")
            booleankey = False
            for i in chosenWord:
                if i in repeat:
                    print(f'{i} ', end="")
                else:
                    print("_ ", end="")
                    booleankey = True
            print()
        else:
            print("\033[31mEssa letra nao tem!")
            chances -= 1
    else:
        print("\033[35mEssa letra ja foi digitada.")
    
    
    if chances<=0:
        print("\033[31mSuas chances acabaram! O homem morreu!")
        break

if booleankey == False:
    print(f"\033[32mParabéns! Voce salvou o homem! Resposta: {chosenWord}")
print ("\033[31mGAME OVER!")
    
    
