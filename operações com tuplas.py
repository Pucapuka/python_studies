#Tupla
#O que difere as tuplas da lista: a tupla não pode ser modificada. 

times_brasileiros = ('Palmeiras', 'Flamengo', 'Vasco', "Grêmio")  #declarando uma Tupla
print(type(times_brasileiros)) #apresentando o tipo da Tupla
print(times_brasileiros) #apresenta a Tupla

print (times_brasileiros[2]) #acessando um elemento da tupla

#diferindo uma string de uma tupla unitária

time_rubro_negro_str=('flamengo') #isso é uma string
time_rubro_negro_tpl=('flamengo',) #isso é uma tupla

print(type(time_rubro_negro_str))
print(type(time_rubro_negro_tpl))
