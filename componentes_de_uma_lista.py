#Numerar componentes de uma lista, ler e apresentar esses componentes

i = 0
quantidadeDePessoas = int (input("Quantas pessoas compõem a lista: "))
nomes = []

while i < quantidadeDePessoas:
    nome= input ("Digite o nome do {}o componente: ".format(i+1))
    i = i + 1
    nomes.append(nome)
    
print ("Os nomes da lista são: ", nomes)
