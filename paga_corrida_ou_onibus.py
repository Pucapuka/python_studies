dinheiroDisponivel = 8.30

valorCorrida = input("Quanto custa a corrida? ")
if float(valorCorrida) <= (dinheiroDisponivel):
    print("Pegar a corrida.")
    
elif (float(valorCorrida) > dinheiroDisponivel) and (float (valorCorrida) <= (dinheiroDisponivel * 3)):
    print ("Espera passar um com melhor valor.")
else: 
    print ("Pega um ônibus.")
    


