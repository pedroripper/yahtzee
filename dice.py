import interface as it
import random

__all__ = ['createSeq', 'removeDicesFromSeq']

def tossDice():
	lDado = random.randint(1,6)
	return lDado

def removeDicesFromSeq(seq, diceIndexes):
	newSeq = []
	newSeq[:] += seq
	for i in range(len(diceIndexes)):
		newSeq.remove(seq[diceIndexes[i]])
	return newSeq


def selectDicesToRollAgain(seq, chances):
	selectedDicesInput = []
	diceIndexes = []
	print("Qual o numero de dados que deseja jogar novamente?\n")
	nDices = int(input())
	print("Dados que voce pode jogar novamente\n")
	for j in range(len(seq)):
			print(str(seq[j]) + "-->(" + str(j+1) + ") \n")
	for k in range(nDices):
		print("Escolha o " + str(k + 1) + "o dado para trocar")
		selected = int(input())
		selectedDicesInput[:] += [int(selected)]
	 #Jogador escolhe os dados que ele deseja jogar novamente
	print(selectedDicesInput)
	for i in range(len(selectedDicesInput)):
		diceIndexes[:] += [int(selectedDicesInput[i]) - 1] #Passa o input de string para uma list de int, ajustando o index dos dados
	seq [:] = removeDicesFromSeq(seq, diceIndexes) #Chama a funcao que remove os dados nao desejados
	return seq


def createSeq():
	chances = 3
	dicesToRoll = 5
	seq = []
	chanceSeq = []

	while(chances >=  0):
		chances -= 1

		print('PREENCHENDO SEQ')
		for i in range(dicesToRoll):
			chanceSeq[:] += [tossDice()] #cria a sequencia com dados aleatorios de 1 a 6
		print(chanceSeq)
		
		it.displayDices(chanceSeq, chances) #Exibe os dados na interface
		chanceSeq[:] = it.finalSeq # Pega os dados que o usuario desejou
		print(chanceSeq)
		dicesToRoll = 5 - len(chanceSeq) #Dados a serem jogados sao 5 - (numero de dados que quis ficar)
		if(dicesToRoll == 0): # Se nao tem dados para jogar, usuario quis ficar com todos, logo nao vai mudar seq
			it.displayDices(chanceSeq, 0)
			chances = 0
			break

	return chanceSeq

