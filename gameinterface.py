# 
# Nesse modulo constam as funcoes dos elementos da interface relacionados
# a partida 
# 

from tkinter import *
from PIL import ImageTk, Image
from cellmanager import *
import gamemanager as gm
from menubar import *
import interface as it
from dicemanager import *

__all__ = ['startGameView','loadGameElements','updateGameStatus','removeGameElements']


def startGameView(root):
	global mainRoot
	global gameFrame
	mainRoot = root
	gameFrame = Frame(mainRoot)

	global gameCanvas
	gameCanvas = Canvas(gameFrame, width=500, height=80, bg='white')  

	global roundLabel
	global playerTurnLabel
	roundLabel = Label(gameFrame, text = '', font=('Times', 20))
	playerTurnLabel = Label(gameFrame, text = '', font=('Times', 20))

	global tossDicesButton
	global choiceTossDice
	choiceTossDice = ImageTk.PhotoImage(Image.open("images/tossDices.png"))
	tossDicesButton = gameCanvas.create_image(250, 5, image=choiceTossDice, anchor=CENTER, tags = 'tossDicesTag', state = 'hidden')

	choiceTossDiceSize = [choiceTossDice.width(), choiceTossDice.height()]
	choiceTossDicePos = [gameCanvas.coords('tossDicesTag')[0] - choiceTossDiceSize[0]/2, gameCanvas.coords('tossDicesTag')[1] - choiceTossDiceSize[1]/2]


	def gameCanvasClick(event):
		print("aas")
		choiceTossDicePos[:] = [gameCanvas.coords('tossDicesTag')[0] - choiceTossDiceSize[0]/2, gameCanvas.coords('tossDicesTag')[1] - choiceTossDiceSize[1]/2]
# 	Jogo ja comecou
		if(gm.getGameRound() >= 13):
			return
# 	Usuario escolhe lancar os dados
		elif(event.x >= choiceTossDicePos[0] and event.x <= (choiceTossDicePos[0]+choiceTossDiceSize[0])):
			if(event.y >= choiceTossDicePos[1] and event.y <= (choiceTossDicePos[1]+choiceTossDiceSize[1])):
				gameCanvas.pack_forget()
				gameFrame.pack(side = TOP)
				chooseCell(gm.getPlayerTurn(), createSeq())
				status = gm.gameUpdate()
				if(status != None):
					gameFrame.pack_forget()
					winnerLabel = Label(root, text = 'O jogador %s ganhou!' % (gm.getPlayerNamesInd(status)), font=('Times', 20))
					winnerPointsLabel = Label(root, text = 'Foram %d pontos!' % (gm.getWinnerPoints()), font=('Times', 20))
					winnerLabel.pack()
					winnerPointsLabel.pack()
					return

	gameCanvas.bind("<Button-1>", gameCanvasClick) #evento de clique do mouse

# 
# Carrega os principais elementos para a partida
# 
def loadGameElements(isNewGame): 
	global mainRoot
	global gameCanvas
	global gameFrame
	global gameState
	global namesLabel
	global choiceTossDice

	gameFrame.pack()
	roundLabel.pack()
	playerTurnLabel.pack()
	gameCanvas.pack()
	gameCanvas.itemconfigure(tossDicesButton, state = 'normal')
	
	it.removeStarterViewElements(isNewGame)
	
	setUpTableMenubar(mainRoot)

	updateGameStatus()


# 
# Atualiza o status do jogo na interface
# 
def updateGameStatus(): # atualiza na interface a rodada e a vez do jogador\
	global roundLabel
	global gameCanvas
	global playerTurnLabel
	global tossDicesButton

	gameCanvas.coords(tossDicesButton, ((250)), 50)

	turn = gm.getPlayerTurn()
	roundLabel.config(text = 'Rodada número: %d' % (gm.getGameRound()+1))
	playerTurnLabel.config(text = 'Vez do jogador: ' + gm.getPlayerNamesInd(turn))
	gameCanvas.pack(side = BOTTOM)
	roundLabel.pack()
	playerTurnLabel.pack()


def removeGameElements():
	global playerTurnLabel
	global roundLabel

	playerTurnLabel.pack_forget()
	roundLabel.pack_forget()








