# 
# Nesse modulo constam as funcoes relacionadas ao menubar
# do jogo, onde e possivel salvar/carregar o jogo e 
# exibir a tabela de usuario
# 

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tablemanager as tm
from filemanager import*
import gameinterface as gi
import gamemanager as gm
import cellmanager as cm

__all__ = ['setUpFileMenubar','setUpTableMenubar','setUpAdmMenubar']

# 
# Cria a secao de save/load para o menubar
# 
def setUpFileMenubar(root):
	global menubar
	# fileMenu = Menu(menubar, tearoff = False)
	fileMenu = Menu(menubar, tearoff = False)
	fileMenu.add_command(label="Carregar", command=loadGame)
	fileMenu.add_command(label="Salvar", command=lambda : saveGame(gm.getNumberPlayers(), gm.getPlayerTurn(), gm.getGameRound()))
	menubar.add_cascade(menu = fileMenu, label = "Partida")
	root.config(menu=menubar)

# 
# Cria a secao de tabela dos usuarios na menubar
# 
def setUpTableMenubar(root):
	global menubar
	tableMenu = Menu(menubar, tearoff = False)
	for i in range(gm.getNumberPlayers()): 
		if(i == 0):
			tableMenu.add_command(label=gm.getPlayerNamesInd(i), command=lambda : menuBarTableSelect(0))
		if(i == 1):
			tableMenu.add_command(label=gm.getPlayerNamesInd(i), command=lambda : menuBarTableSelect(1))
		if(i == 2):
			tableMenu.add_command(label=gm.getPlayerNamesInd(i), command=lambda : menuBarTableSelect(2))
		if(i == 3):
			tableMenu.add_command(label=gm.getPlayerNamesInd(i), command=lambda : menuBarTableSelect(3))
		if(i == 4):
			tableMenu.add_command(label=gm.getPlayerNamesInd(i), command=lambda : menuBarTableSelect(4))
		if(i == 5):
			tableMenu.add_command(label=gm.getPlayerNamesInd(i), command=lambda : menuBarTableSelect(5))
	menubar.add_cascade(menu = tableMenu, label = "Tabelas")

# 
# Cria a secao de inserir sequencia de dados para o administrador
# 
def setUpAdmMenubar(root):
	global menubar
	menubar = Menu(root)
	admMenu = Menu(menubar, tearoff = False)
	admMenu.add_command(label="Inserir sequencia", command=runAdmCommand)
	menubar.add_cascade(menu = admMenu, label = "Adm")

# 
# Administrador insere a sequencia de dados desejada
# 
def runAdmCommand():
	print("Modo Administrador\n")
	print("Insira a sequencia de dados\n")
	admInput = input()
	seqAdm = []
	for i in admInput:
		seqAdm += [int(i)]
	gi.removeButtonInAdmMode()
	cm.chooseCell(gm.getPlayerTurn(), seqAdm)
	gm.gameUpdate()



# 
# Chama getUserTable para exibir a tabela do usuario desejado
# 
def menuBarTableSelect(i): 
	tm.getUserTable(i)



