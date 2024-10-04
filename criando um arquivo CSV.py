import csv

with open ('users.csv', 'w') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(["nome", "sobrenome", "email", "gênero"])
    escritor.writerow(["Pietro", "Ribeiro", "pietro@email.com", "masculino"])

#O código criou o arquivo "users.csv"
