#Exercício de laços de repetição

#com uma lista

Alunos = ['Carlos', 'Anderson', 'Junior', 'Pedro']
for nome in Alunos:    #laço de repetição usando o for
    print (nome)
print ("- "*50)

i=0
while i < len(Alunos):   #laço de repetição usando o while
    print(Alunos[i])
    i = i + 1

print("-"*100)

#com uma tupla
Alunos = 'Carlos', 'Anderson', 'Junior', 'Pedro'
for nome in Alunos:                     
    print (nome)                #laço for
print("-"*100)

#com um dicionário
Cliente = {
    "nome" : "Paulo" ,
    "data de nascimento": "06/07/1987",        #estruturação do dicionario, pode ser assim ou em uma linha só
    "endereço" : "Rua da Assembleia, 3."
}

#Para representar o laço de repetição com a lista do dicionario, eu posso utilizar uma palavra qualquer (nessa caso, usei "mac")
# e coloco, em seguida, no outro lado, qual o valor representaria esse dado no dicionário "Cliente".

for mac in Cliente:
    print(f"{mac}:{Cliente[mac]}")

print ("-"*100)

#trabalhando laço em ranges

for numero in range (10): #vai listar de 0 a "10-1"
    print (numero)
print ("-" *50)    
for numero in range (3,10):  #vai listar de 3 a "10-1"
    print (numero)
print ("-"*50)    
for numero in range (2,10,2): #vai listar de 2  "10-1", de dois em dois.
    print (numero)
print ("-"*50)
for numero in range (10, 0, -1): #vai listar de 10 a "0+1" de -1 em -1
    print (numero)
