import random

wordList = ("mudar", "imergir", "estrangeiro", "pais")
repeat = []
chosenWord = random.choice(wordList)
chances = 6
booleankey = True

print ("Jogo da forca. Adivinhe a palavra letra a letra. Você tem 6 chances!")

while True:
  if booleankey == False:
      break
  else:
    chosenLetter = input("Digite uma letra: ")
    if chosenLetter not in repeat:
        repeat.append(chosenLetter)
        if chosenLetter in chosenWord:
            print("Voce achou uma letra!")
            booleankey = False
            for i in chosenWord:
                if i in repeat:
                    print(i, end="")
                else:
                    print("_", end="")
                    booleankey = True
            print()
        else:
            print("Essa letra nao tem!")
            chances -= 1
    else:
        print("Essa letra ja foi digitada.")
    
    
    if chances<=0:
        print("Suas chances acabaram! O homem morreu!")
        break

if booleankey == False:
    print(f"Parabéns! Voce salvou o homem! Resposta: {chosenWord}")
print ("GAME OVER!")
    
