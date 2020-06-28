# 
# Nesse modulo constam as funcoes relacionadas a salvar
# e carregar o jogo
# 

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from gamemanager import*
from tablemanager import *
import interface as inter
__all__ = ['saveGame','loadGame']


#
# Salva no arquivo txt o numero de jogadores, nomes, vez do jogador, rodada da partida
# e as tabelas de cada jogador
# 
def saveGame(nPlayers, pTurn, gRound):
	messagebox.showinfo("Aviso", "Se você salvar durante a sua vez vai perder os dados que jogou")
	save = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
	if save is None:
		return
	formatedPnameList = ""
	for i in range(6):
		formatedPnameList += (getPlayerNamesInd(i)) + " "
	save.write("Dados da partida\n")
	save.write(str(getNumberPlayers()) + '\n')
	save.write(formatedPnameList + '\n')
	save.write(str(getPlayerTurn()) + '\n')
	save.write(str(getGameRound()) + '\n')
	for j in range(int(getNumberPlayers())):
		save.write(prepareTableToSave(j) + "\n")
	save.close()

#
# Recebe do arquivo txt o numero de jogadores, nomes, vez do jogador, rodada da partida
# e as tabelas de cada jogador
# 
def loadGame():
	load = filedialog.askopenfilename(initialdir = "file:///",title = "Escolha o arquivo",filetypes = (("txt files","*.txt"),("all files","*.*")))	
	file = open(load)
	file.readline()

	loadedTable = []
	fileText = file.readline() #pegando o numero de jogadores
	setNumberPlayers(int(fileText[:(len(fileText)-1)]))
	fileText = file.readline() #pegando os nomes dos jogadores
	formatedPnameList = (fileText[:(len(fileText)-1)])
	setPlayerNames(formatedPnameList)
	fileText = file.readline() #pegando a vez do jogador
	setPlayerTurn(int(fileText[:(len(fileText)-1)]))
	fileText = file.readline() #pegando o numero da rodada
	setGameRound(int(fileText[:(len(fileText)-1)]))
	for i in range(getNumberPlayers()):
		fileText = file.readline() #pegando a tabela do jogador i
		loadedTable += [fileText.split()]
	loadTable(loadedTable)
	inter.loadGameElements(False)

