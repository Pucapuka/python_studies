
#lista
programadores = ["Emmanuel", 'Paulo', 'Ian', 'Ester']
print (type(programadores)) #mostar o tipo
print (len(programadores)) #mostrar o tamanho da lista
print(programadores[2]) #mostrar o elemento 2 da lista

programadores[3]="Sara" #mudar o elemento 3 (que era Ester e agora é Sara)
print(programadores[3]) #apresentar o elemento 3 da lista
programadores.append('Ester') #adicionar elemento no final da lista
print(programadores) #mostra a lista toda
programadores.insert(2, "Mellanie") #adiciona o elemento "Mellanie" na posição 2 da lista 
print(programadores)
programadores.remove("Mellanie") #elimina o elemento pelo nome
print(programadores)
programadores.pop(4) #elimina o elemento de índice 4 na lista (no caso, Ester)
print(programadores)


