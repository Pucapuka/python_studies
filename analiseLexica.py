#codigo a ser analisado
code = "position=initial+rate*60"

#variável que armazena cada lexema
lexema = ""

#pequena gambiarra para não dar erro de vazamento no array
code = code + " "

#loop para imprimir os tokens
for i in range(0,len(code)):
    if code[i].isalpha() :
        lexema += code[i]
        
        if code[i+1].isspace() or code[i+1] in ("+", "-", "*", "/", "="):
            print(f"<ID, {lexema}>")
            lexema = ""
    
    elif code[i] in ("+", "-", "*", "/", "="):
        lexema += code[i]
        print(f"<OP, {lexema}>")
        lexema = ""
            
    elif code[i].isnumeric():
        lexema += code[i]
        if code[i+1].isspace() or code[i+1] in ("+", "-", "*", "/", "="):
            print(f"<NUM, {lexema}>")
            lexema = ""
