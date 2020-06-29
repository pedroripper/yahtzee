# 
# Nesse modulo constam as funcoes relacionadas a
# administracao das celulas
# 
import tablemanager as tm
import cellinterface as ci


__all__ = ['chooseCell','calcPlays']

# 
# Calcula jogada em todas as celulas
# 
def calcPlays(lD, nPlayer): 
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
	if 3 in lS or 4 in lS or 5 in lS:
		n3iguals = sum(lD)
	dF[6] = n3iguals

	#4 iguais
	n4iguals = 0
	if 4 in lS or 5 in lS:
		n4iguals = sum(lD)
	dF[7] = n4iguals

	#Full House
	nFull = 0
	if 3 in lS and 2 in lS:
		nFull = 25
	dF[8] = nFull

	#Seq Min
	nMin = 0
	if (lS[0]>0 and lS[1]>0  and lS[2]>0 and lS[3]>0) or (lS[1]>0 and lS[2]>0 and lS[3]>0 and lS[4]>0) or (lS[2]>0 and lS[3]>0 and lS[4]>0 and lS[5]>0):
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
		if(tm.canYahtbonus(nPlayer)):
			dF[13] = 1
	dF[11] = nYahtzee

	#chance
	nChance = 0
	nChance = sum(lD)
	dF[12] = nChance

	return dF

# 
# Faz o usuario escolher a celula desejada
# 
def chooseCell (nPlayer, lD):

	nCel = 0
	dCelulas = calcPlays(lD, nPlayer);


	ci.chooseCellEntry(dCelulas)

	cel = ci.getSelectedCell()
	if cel == 'um': 
		nCel = 0
	elif cel == 'dois': 
		nCel = 1
	elif cel == 'tres': 
		nCel = 2
	elif cel == 'quatro': 
		nCel = 3
	elif cel == 'cinco': 
		nCel = 4
	elif cel == 'seis': 
		nCel = 5
	elif cel == 'trinca': 
		nCel = 6
	elif cel == 'quadra': 
		nCel = 7
	elif cel == 'fullhouse' or cel == 'full house': 
		nCel = 8
	elif cel == 'minima' or cel == 'seq min': 
		print("porr")
		nCel = 9
	elif cel == 'maxima' or cel == 'seq max': 
		nCel = 10
	elif cel == 'yahtzee': 
		if(tm.canYahtbonus(nPlayer)):
			nCel = 13
		else:
			nCel = 11
	elif cel == 'chance': 
		nCel = 12
	elif cel == 'pass': 
		return
	
	val = dCelulas[nCel]
	
	cellCheck = tm.insertValue(nPlayer, nCel, val)
	if cellCheck == False:
		print("\nErro na escolha de celula. Tentando novamente...\n")
		chooseCell(nPlayer,lD)

	return

