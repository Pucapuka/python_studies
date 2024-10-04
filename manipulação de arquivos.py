#manipulação de arquivos
with open("arquivo.txt", 'w', encoding='utf-8') as arquivo:
    arquivo.write("Essa é a primeira linha\n")                  #criando um arquivo de texto.txt
    arquivo.write("Essa é a segunda linha\n")
    
with open("arquivo.txt", 'r', encoding='utf-8') as arquivo:     #lendo esse arquivo
    print(arquivo.read())
    
