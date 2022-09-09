#!/usr/bin/python3

#Coding For Security - Programa BodyHealth
#Versão: 1.0.0.
#Autora: Emmanuelle Louise Corrá
#Turma: 1TDCA
#RM: 93392 
#Professor Fábio Pires

#A manutenção de um corpo saudável, se da pela criação de hábitos saudáveis relacionados a alimentação, prática de exercicios e qualidade de sono.
#O programa pode ser usado para medir sua saúde daqui alguns anos, principalmente focado em 30 anos.
#O programa contém foco do usuário em atividade fisica, tempo dormido, alimentação saudável com frutas, vegetais e vitamina natural d.
#O programa solicita cada informação para o usuário preencher conforme a preferencia.
#Saudavel - Estável - Sem saúde (estragado) 

from sklearn import tree

print('==========Bem vindo, gostaria de verificar a sua saúde hoje?==========')

#variaveis 
cotidiano = '1'
raramente = '2'
nunca = '3'
saudável = '1'
estável = '2'
semsaude = '3'

saude=[["10","30", cotidiano, cotidiano, cotidiano], ['15', '5', raramente, raramente, raramente], ['4','7', nunca, nunca, nunca]]

resultado=[saudável, estável, semsaude] #variaveis

#tree sklearn
classificador=tree.DecisionTreeClassifier()
classificador=classificador.fit(saude,resultado)

#perguntas aos usuário
atividadefisica=input('Quanto de exercícios físico você faz? ')
temposono=input('Quanto tempo você dorme? ') 
comidasaudavel= input('Qual a frequência que você ingere frutar? 1-cotidiano, 2-raramente ou 3-nunca: ')
refeiçoes=input('Qual é a frequência que você faz refeições saúdaveis? 1-cotidiano, 2-raramente ou 3-nunca: ')
vitaminad= input('Qual a frequência que toma sol? 1-cotidiano, 2-raramente ou 3-nunca: ')

resultadousuario=classificador.predict([[atividadefisica, temposono, comidasaudavel, refeiçoes, vitaminad]])

#decisão de resultado, conforme as resposta do usuário 
if resultadousuario == '1':
	print('Seu corpo daqui 30 anos estará saúdavel!')
elif resultadousuario == '2':
	print('Seu corpo daqui 30 anos estará normal!')
elif resultadousuario == '3':
	print('Seu corpo daqui 30 anos estará sem saúde')
else:
	print('Invalido!')  #Respostas inválidas
