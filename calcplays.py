# 
# Nesse modulo constam as funcoes de calculo dos valores das celulas
# 
# 

__all__ = ['calcPlays']


def calcPlays(lD): # calcular jogada em todas as celulas
	lS = []
	dF = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	#Superior
	#um
	nOne = lD.count(1)
	lS.append(nOne)
	dF[0] = nOne*1 

	#dois
	nTwo = lD.count(2)
	lS.append(nTwo)
	dF[1] = nTwo*2

	#tres
	nTree = lD.count(3)
	lS.append(nTree)
	dF[2] = nTree*3

	#quatro
	nFour = lD.count(4)
	lS.append(nFour)
	dF[3] = nFour*4

	#cinco
	nFive = lD.count(5)
	lS.append(nFive)
	dF[4] = nFive*5 

	#seis
	nSix = lD.count(6)
	lS.append(nSix)
	dF[5] = nSix*6


	#Inferior

	#3 iguais
	n3iguals = 0
	if 3 in lS:
		n3iguals = sum(lS)
	dF[6] = n3iguals

	#4 iguais
	n4iguals = 0
	if 4 in lS:
		n4iguals = sum(lS)
	dF[7] = n4iguals

	#Full House
	nFull = 0
	if 3 in lS and 2 in lS:
		nFull = 25
	dF[8] = nFull

	#Seq Min
	nMin = 0
	if lS.count(1) >= 3:
		if lS.count(2) != 0:
			if lS[0] == 0 and (lS[1] == 0 or lS[-1] ==0):
				nMin = 30
			if lS[-1] == 0 and lS[-2] == 0:
				nMin = 30
		else:
			if lS[-2] == 0 or lS[1] == 0:
				nMin = 30
	dF[9] = nMin

	#Seq Maxima
	nMax = 0
	if lS.count(1) == 5:
		if lS[0] == 0 or lS[-1] == 0:
			nMax = 40
	dF[10] = nMax

	#yahtzee
	nYahtzee = 0
	if lS.count(5) == 1:
		nYahtzee = 50
	dF[11] = nYahtzee

	#chance
	nChance = 0
	nChance = sum(lD)
	dF[12] = nChance

	dF[13] = 0
	return dF

