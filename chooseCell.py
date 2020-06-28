from dice import *
from calcplays import *
from tablemanager import *
import interface as it


__all__ = ['chooseCell']

def chooseCell (nPlayer, lD):

	print(lD)

	lOptions = ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'trinca', 'quadra', 'fullhouse', 'minima', 'maxima', 'yathzee', 'chance']
	nCel = 0
	dCelulas = calcPlays(lD);


	it.chooseCellEntry(dCelulas)

	cel = it.getSelectedCell()
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
	elif cel == 'fullhouse': 
		nCel = 8
	elif cel == 'minima': 
		nCel = 9
	elif cel == 'maxima': 
		nCel = 10
	elif cel == 'yathzee': 
		nCel = 11
	elif cel == 'chance': 
		nCel = 12

	val = dCelulas[nCel]
	
	cellCheck = insertValue(nPlayer, nCel, val)
	if cellCheck == False:
		print("\nErro na escolha de celula. Tentando novamente...\n")
		chooseCell(nPlayer,lD)

	return

