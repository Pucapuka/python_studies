Cliente = {
    "nome" : "Paulo" ,
    "data_nascimento": "06/07/1987",        #estruturação do dicionario, pode ser assim ou em uma linha só
    "endereco" : "Rua da Assembleia, 3."
}

Cliente["raça"]= "branca"        #adicionando mais dados ao dicionário
Cliente["idade"]= "35 anos"

chaves = Cliente.keys()          #coloquei as chaves do dicionário na variável "chave" para apresentar depois
valores = Cliente.values()      #coloquei os valores do dicionário na variável "valores" para apresentar depois
itens = Cliente.items()         #coloquei os dois (chaves e valores) do dicionário na variável "itens" para apresentar depois

print (Cliente)  #veja que já terá os dados do dicionario do começo e os dois dados adicionados
print (chaves)
print (valores)
print (itens)

print ("-"*100)

Cliente['raça'] = 'parda'   #alterando um valor dentro de uma chave que já consta no dicionário
print (Cliente)             #veja como mudou

print ("-"*100)

#copiando um dicionario

Cliente2 = Cliente.copy()
print (Cliente2)

print ("-"*100)

#alterando a copia (sem alterar o original)

Cliente2['nome'] = 'Arthur'
Cliente2['data_nascimento']= '27/07/2016'
Cliente2['endereco'] = 'Rua da Assembleia, 3.'
Cliente2['idade'] = '6 anos.'

print (Cliente) 
print (Cliente2)  #viu como só ele alterou?

print ("-"*100)

print(Cliente ['raça']) #consultando um dado específico do dicionário
print (Cliente.get("idade")) #outra forma de consulta de um dado específico do dicionário
