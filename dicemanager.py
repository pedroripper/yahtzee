# 
# Nesse modulo constam as funcoes responsaveis por administrar as atividades dos
# dados nao relacionadas a interface
# 
import interface as it
import random

__all__ = ['createSeq']

# 
# Gera dados aleatorios de 1 a 6
# 
def tossDice():
	lDado = random.randint(1,6)
	return lDado

# 
# Cria sequencia de dados, seguindo o numero de chances que o usuario tem
# 
def createSeq():
	chances = 3
	dicesToRoll = 5
	seq = []
	chanceSeq = []
	while(chances >=  0):
		chances -= 1
		for i in range(dicesToRoll):
# 	Cria a sequencia com dados aleatorios de 1 a 6
			chanceSeq[:] += [tossDice()] 
#	Exibe os dados na interface
		it.displayDices(chanceSeq, chances) 
# 	Pega os dados que o usuario desejou
		chanceSeq[:] = it.getFinalSeq() 
#	Dados a serem jogados sao 5 - (numero de dados que quis ficar)
		dicesToRoll = 5 - len(chanceSeq) 
# 	Se nao tem dados para jogar, usuario quis ficar com todos, logo nao vai mudar seq
		if(dicesToRoll == 0): 
			it.displayDices(chanceSeq, 0)
			chances = 0
			break

	return chanceSeq

