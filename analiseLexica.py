code = "position = initial + rate * 60 "
lexema = ""

for i in range(0,len(code)):
    if code[i].isalpha() :
        lexema += code[i]
        
        if code[i+1].isspace():
            print(f"<ID, {lexema}>")
            lexema = ""
    
    elif code[i] in ("+", "-", "*", "/", "="):
        lexema += code[i]
        
        if code[i+1].isspace():
            print(f"<OP, {lexema}>")
            lexema = ""
            
    elif code[i].isnumeric():
        lexema += code[i]
        if code[i+1].isspace() or None:
            print(f"<NUM, {lexema}>")
            lexema = ""
        # else:
        #     print(f"<NUM, {lexema}>")
        #     lexema = ""
