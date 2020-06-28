# 
# Nesse modulo constam as funcoes relacionadas ao menubar
# do jogo, onde e possivel salvar/carregar o jogo e 
# exibir a tabela de usuario
# 

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tablemanager import*
from filemanager import*
from gamemanager import*
__all__ = ['setUpFileMenubar','setUpTableMenubar']

# 
# Cria a secao de save/load para o menubar
# 
def setUpFileMenubar(root):
	global menubar
	menubar = Menu(root)
	# fileMenu = Menu(menubar, tearoff = False)
	fileMenu = Menu(menubar, tearoff = False)
	fileMenu.add_command(label="Carregar", command=loadGame)
	fileMenu.add_command(label="Salvar", command=lambda : saveGame(getNumberPlayers(), getPlayerTurn(), getGameRound()))
	menubar.add_cascade(menu = fileMenu, label = "Partida")
	root.config(menu=menubar)

# 
# Cria a secao de tabela dos usuarios na menubar
# 
def setUpTableMenubar(root):
	global menubar
	numPlayers = getNumberPlayers()
	tableMenu = Menu(menubar, tearoff = False)
	for i in range(numPlayers): 
		if(i == 0):
			tableMenu.add_command(label=getPlayerNamesInd(i), command=lambda : menuBarTableSelect(0))
		if(i == 1):
			tableMenu.add_command(label=getPlayerNamesInd(i), command=lambda : menuBarTableSelect(1))
		if(i == 2):
			tableMenu.add_command(label=getPlayerNamesInd(i), command=lambda : menuBarTableSelect(2))
		if(i == 3):
			tableMenu.add_command(label=getPlayerNamesInd(i), command=lambda : menuBarTableSelect(3))
		if(i == 4):
			tableMenu.add_command(label=getPlayerNamesInd(i), command=lambda : menuBarTableSelect(4))
		if(i == 5):
			tableMenu.add_command(label=getPlayerNamesInd(i), command=lambda : menuBarTableSelect(5))
	menubar.add_cascade(menu = tableMenu, label = "Tabelas")

# 
# Chama getUserTable para exibir a tabela do usuario desejado
# 
def menuBarTableSelect(i): 
	print("Mostra a tabela do usuario " + str(i+1))
	getUserTable(i)



