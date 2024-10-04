#funções

def hello():                  #essa função não precisará de um conteúdo dentro dos parêntesis
    print("Olá, mundo!")  

hello()

print ("-"*100)

def soma(v1,v2,v3):         #já essa função precisa de conteúdo nos parêntesis
    soma = v1 + v2 + v3
    print(soma)

(soma (2,3,4))              #o conteúdo é reiterado com os dados a ocuparem aquelas variáveis

print ("-"*100)

def media(v1,v2,v3):
    soma= v1+v2+v3
    media = soma / 3
    print(media)

media(5,6,7)

print ('-' *100)

def dadosPessoais(nome, idade, cidade):
    print("Seu nome é {}, você tem {} anos e mora em {}.".format(nome, idade, cidade))

dadosPessoais("José", 30, "Maceió")       # Saída: Seu nome é José, você tem 30 anos e mora em Maceió.

#Outra forma

def dadosPessoais(nome="José", idade=30, cidade="Maceió"):
    print(f"Seu nome é {nome}, você tem {idade} anos e mora em {cidade}.")
dadosPessoais()

print('-'*100)

def somatorio(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma

numeros = [1, 2, 3, 4, 5,6,7,8,9]
soma_dos_numeros = somatorio(numeros)
print("A soma dos elementos da lista vale: ", soma_dos_numeros)

if somatorio(numeros) > 50:
    print("Que soma grande!")
else:
    print("Que soma pequena!")
