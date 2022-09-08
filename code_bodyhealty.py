#!/usr/bin/python3

#Emmanuelle Louise Corrá
#1TDCA
#RM: 93392 

from sklearn import tree

print('==========Bem vindo, gostaria de verificar a sua saúde hoje?==========')

cotidiano = '1'
raramente = '2'
nunca = '3'
saudável = '1'
estável = '2'
semsaude = '3'

saude=[["10","30", cotidiano, cotidiano, cotidiano], ['15', '5', raramente, raramente, raramente], ['4','7', nunca, nunca, nunca]]

resultado=[saudável, estável, semsaude]

classificador=tree.DecisionTreeClassifier()
classificador=classificador.fit(saude,resultado)

atividadefisica=input('Quanto de exercícios físico você faz? ')
temposono=input('Quanto tempo você dorme? ') 
comidasaudavel= input('Qual a frequência que você ingere frutar? 1-cotidiano, 2-raramente ou 3-nunca: ')
refeiçoes=input('Qual é a frequência que você faz refeições saúdaveis? 1-cotidiano, 2-raramente ou 3-nunca: ')
vitaminad= input('Qual a frequência que toma sol? 1-cotidiano, 2-raramente ou 3-nunca: ')

resultadousuario=classificador.predict([[atividadefisica, temposono, comidasaudavel, refeiçoes, vitaminad]])

if resultadousuario == '1':
	print('Seu corpo daqui 30 anos estará saúdavel!')
elif resultadousuario == '2':
	print('Seu corpo daqui 30 anos estará normal!')
elif resultadousuario == '3':
	print('Seu corpo daqui 30 anos estará sem saúde')
else:
	print('Invalido!')
