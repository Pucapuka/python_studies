#Fazer um algoritmo em python que peça a quantidade de números de uma lista e que, logo após, liste os números que a comporão, apresentando-os e dando a opção de ir removendo-os:

numeros = []
lista = int (input("Quantos números caberão na lista?")) 
i=0

while i<lista:                                #laço de repetição
    numero = input ("digite um número: ")     #número para inserir na lista
    numeros.append(numero)                    #inserção desse número
    i = i+1                                   #contagem até dar o número de componentes da lista

print(numeros)

resposta = 'S'
while resposta == 's' or resposta == 'S':                   #Laço interativo para repetir enquanto o usuário quiser
    rm = input("qual número da lista você quer remover?")   
    numeros.remove(rm)
    print (numeros)
    resposta = input ("Quer remover mais algum (S/N)?")
