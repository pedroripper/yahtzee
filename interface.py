# 
# Nesse modulo constam as funcoes da tela principal do jogo
# 
# 
from tkinter import *
from PIL import ImageTk, Image
from tablemanager import*
from dice import*
from chooseCell import*
from menubar import*
from gamemanager import*


__all__ = ['mainView', 'displayDices','getFinalSeq','chooseCellEntry']


root = Tk()

dicesFrame = Frame(root)
diceCanvas = Canvas(dicesFrame, width=500, height=150, bg='white')
chancesLabel = Label(dicesFrame, text = "Chances: %d" % 0,  font=('Times', 20), compound = "center")

# 
# Escolhe a celula que deseja inserir na interface
# 
def chooseCellEntry(dCelulas): 
	entryFrame = Frame(root)
	entryFrame.pack()
	entry = Entry(entryFrame)
	entryCanvas = Canvas(entryFrame, width=250, height=100, bg='white')
	entryLabel = Label(entryFrame, text = "Escolha a célula",  font=('Times', 20), compound = "center")
	entryFrame.pack()
	entryLabel.pack()
	entry.pack()
	entryCanvas.pack()
	confirmImage = ImageTk.PhotoImage(Image.open("images/confirm.png"))
	entryCanvas.create_image(125, 50, image=confirmImage, anchor=CENTER, tags='checkCellButton')

# 
# 	Pega o valor da celula decidida pelo usuario
# 
	def cellChoice(event):
		global selectedCell
		global dicesFrame
		selectedCell = ""
		confirmImageSize = [confirmImage.width(), confirmImage.height()]
		confirmButtonPos = [entryCanvas.coords('checkCellButton')[0]-confirmImageSize[0]/2, entryCanvas.coords('checkCellButton')[1]-confirmImageSize[1]/2]
		if(event.x >= confirmButtonPos[0] and event.x <= (confirmButtonPos[0]+confirmImageSize[0])):
				if(event.y >= confirmButtonPos[1] and event.y <= (confirmButtonPos[1]+confirmImageSize[1])):
					selectedCell += entry.get()
					entryCanvas.pack_forget()
					entryLabel.pack_forget()
					entryFrame.pack_forget()
					dicesFrame.pack_forget()
					root.quit()
	entryCanvas.bind("<Button-1>", cellChoice)
	root.mainloop()

# 
# Retorna a celula que o jogador deseja preencher
# 
def getSelectedCell():
	global selectedCell
	return selectedCell


# 
# Exibe os dados lancados pelo usuario para escolher quais lancar novamenrte
# 
def displayDices(seq, chances): 
	
	global diceFrame    
	global diceCanvas
	global chancesLabel
	global finalSeq

	dicesFrame.pack()
	chancesLabel = Label(dicesFrame, text = "Chances: %d" % chances,  font=('Times', 20), compound = "center")
	changeDicesLabel = Label(dicesFrame, text = "Você deseja mudar seus dados?",  font=('Times', 20), compound = "center")

# 	Se ja jogou uma vez limpa av view para exibir de novo
	if(chances < 2): 
		diceCanvas.delete("all")
		chancesLabel.pack_forget()
		diceCanvas.pack_forget()

	diceCanvas.pack(expand=YES, fill=BOTH) 


# 	Dimensoes do diceCanvas
	canvasw = diceCanvas.winfo_width()
	canvash = diceCanvas.winfo_height()

	startedSelectingDices = [False]

# 	Imagem dos dados
	global dice1Image
	global dice2Image
	global dice3Image
	global dice4Image
	global dice5Image
	global dice6Image
	dice1Image = ImageTk.PhotoImage(Image.open("images/dado_1.png"))
	dice2Image = ImageTk.PhotoImage(Image.open("images/dado_2.png"))
	dice3Image = ImageTk.PhotoImage(Image.open("images/dado_3.png"))
	dice4Image = ImageTk.PhotoImage(Image.open("images/dado_4.png"))
	dice5Image = ImageTk.PhotoImage(Image.open("images/dado_5.png"))
	dice6Image = ImageTk.PhotoImage(Image.open("images/dado_6.png"))

# 	Dimensao dos dados
	diceSize =  [dice1Image.width(), dice1Image.height()] 

#	Array de imagens dos dados
	diceImages = [] 

#	Array de posicao dos dados 
	dicePos = [[],[],[],[],[]] #posicao de cada um dos 5 dados

# 	Passa a sequencia final recebida do modulo dicemanager
	finalSeq = seq

# 	Parser para as imagens dos dados e tambem calculo da posicao deles na tela
	for i in range(len(seq)):
		if(seq[i] == 1):
			diceImages += [diceCanvas.create_image(176 + i*42, 50, image=dice1Image, anchor=CENTER)]
		if(seq[i] == 2):
			diceImages += [diceCanvas.create_image(176 + i*42, 50, image=dice2Image, anchor=CENTER)]
		if(seq[i] == 3):
			diceImages += [diceCanvas.create_image(176 + i*42, 50, image=dice3Image, anchor=CENTER)]
		if(seq[i] == 4):
			diceImages += [diceCanvas.create_image(176 + i*42, 50, image=dice4Image, anchor=CENTER)]
		if(seq[i] == 5):
			diceImages += [diceCanvas.create_image(176 + i*42, 50, image=dice5Image, anchor=CENTER)]
		if(seq[i] == 6):
			diceImages += [diceCanvas.create_image(176 + i*42, 50, image=dice6Image, anchor=CENTER)]
		dicePos[i] += [150 + i*42, 34]

# 	Imagens e criacao de imagens no canvas para botoes
	maintainimage = ImageTk.PhotoImage(Image.open("images/confirm.png"))
	changeImage = ImageTk.PhotoImage(Image.open("images/changedices.png"))
	maintainButton = diceCanvas.create_image((250-5) - (maintainimage.width()/2), 120, image=maintainimage, anchor=CENTER, tags = 'maintainButtonTag')
	changeButton = diceCanvas.create_image((250+5) + (changeImage.width()/2), 120, image=changeImage, anchor=CENTER, tags = 'changeButtonTag')
	tossAgainImage = ImageTk.PhotoImage(Image.open("images/tossAgain.png"))
	tossAgainButton = diceCanvas.create_image((250), 120, image=tossAgainImage, anchor=CENTER, tags = 'tossAgainButtonTag', state = 'hidden')

# 	Posicao e dimensao do botoes 
	maintainButtonSize = [maintainimage.width(), maintainimage.height()]
	maintainButtonPos = [diceCanvas.coords('maintainButtonTag')[0] - maintainButtonSize[0]/2, diceCanvas.coords('maintainButtonTag')[1] - maintainButtonSize[1]/2]

	changeButtonSize = [changeImage.width(), changeImage.height()]
	changeButtonPos = [diceCanvas.coords('changeButtonTag')[0] - changeButtonSize[0]/2, diceCanvas.coords('changeButtonTag')[1] - changeButtonSize[1]/2]

	tossAgainButtonSize = [tossAgainImage.width(), tossAgainImage.height()]
	tossAgainButtonPos = [diceCanvas.coords('tossAgainButtonTag')[0] - tossAgainButtonSize[0]/2, diceCanvas.coords('tossAgainButtonTag')[1] - tossAgainButtonSize[1]/2]
	
# 	Se o usuario nao possui mais chances de jogar apenas sao exibidos seus dados finais
	if(chances == 0):
		diceCanvas.itemconfigure(maintainButton, state = 'hidden')
		diceCanvas.itemconfigure(changeButton, state = 'hidden')
		maintainimage = ImageTk.PhotoImage(Image.open("images/confirm.png"))
		confirmButton = diceCanvas.create_image((250), 120, image=maintainimage, anchor=CENTER, tags = 'confirmButtonTag')
		confirmButtonSize = [maintainimage.width(), maintainimage.height()]
		confirmButtonPos = [diceCanvas.coords('confirmButtonTag')[0] - confirmButtonSize[0]/2, diceCanvas.coords('confirmButtonTag')[1] - confirmButtonSize[1]/2]

# 	Decisoes sobre os dados baseados em cliques no canvas
	def dicesChoice(event):
		global diceCanvas
		if(chances == 0):
# 	Confirma a sequencia final de dados
			if(event.x >= confirmButtonPos[0] and event.x <= (confirmButtonPos[0]+confirmButtonSize[0])):
				if(event.y >= confirmButtonPos[1] and event.y <= (confirmButtonPos[1]+confirmButtonSize[1])):
					roundLabel.pack_forget()
					chancesLabel.pack_forget()
					# dicesFrame.pack_forget()
					root.quit()
		else:
# 	Ainda nao comecou a selecionar os dados
			if(startedSelectingDices[0] == 0):
# 	Resolve manter a sequencia de dados
				if(event.x >= maintainButtonPos[0] and event.x <= (maintainButtonPos[0]+maintainButtonSize[0])):
					if(event.y >= maintainButtonPos[1] and event.y <= (maintainButtonPos[1]+maintainButtonSize[1])): 
						dicesFrame.pack_forget()
						root.quit()
# 	Resolve alterar a sequencia de dados
				if(event.x >= changeButtonPos[0] and event.x <= (changeButtonPos[0]+changeButtonSize[0])):
					if(event.y >= changeButtonPos[1] and event.y <= (changeButtonPos[1]+changeButtonSize[1])):
						diceCanvas.itemconfigure(tossAgainButton, state = 'normal')
						diceCanvas.itemconfigure(maintainButton, state = 'hidden')
						diceCanvas.itemconfigure(changeButton, state = 'hidden')
						startedSelectingDices[0] = 1
# 	Ja comecou a alterar a sequencia de dados
			if(startedSelectingDices[0] == 1):
# 	Confirma os dados a serem lancados novamente
				if(event.x >= tossAgainButtonPos[0] and event.x <= (tossAgainButtonPos[0]+tossAgainButtonSize[0])):
					if(event.y >= tossAgainButtonPos[1] and event.y <= (tossAgainButtonPos[1]+tossAgainButtonSize[1])):
						startedSelectingDices[0] = 2
						root.quit()
# 	Seleciona o dado 1
				if(event.x >= dicePos[0][0] + 10 and event.x <= (dicePos[0][0]+42)):
					if(event.y >= dicePos[0][1] and event.y <= (dicePos[0][1]+32)):
						print("Selecionou D1")
						diceCanvas.create_rectangle(dicePos[0][0]+10, dicePos[0][1], dicePos[0][0]+43, dicePos[0][1]+32, outline="#1f1", width = 2)
						finalSeq.remove(seq[0])
# 	Seleciona o dado 2
				if(event.x >= dicePos[1][0] + 10 and event.x <= (dicePos[1][0]+42)):
					if(event.y >= dicePos[1][1] and event.y <= (dicePos[1][1]+32)):
						print("Selecionou D2")
						diceCanvas.create_rectangle(dicePos[1][0]+10, dicePos[1][1], dicePos[1][0]+43, dicePos[1][1]+32, outline="#1f1", width = 2)
						finalSeq.remove(seq[1])
# 	Seleciona o dado 3
				if(event.x >= dicePos[2][0] + 10 and event.x <= (dicePos[2][0]+42)):
					if(event.y >= dicePos[2][1] and event.y <= (dicePos[2][1]+32)):
						print("Selecionou D3")
						diceCanvas.create_rectangle(dicePos[2][0]+10, dicePos[2][1], dicePos[2][0]+43, dicePos[2][1]+32, outline="#1f1", width = 2)
						finalSeq.remove(seq[2])
# 	Seleciona o dado 4
				if(event.x >= dicePos[3][0] + 10 and event.x <= (dicePos[3][0]+42)):
					if(event.y >= dicePos[3][1] and event.y <= (dicePos[3][1]+32)):
						print("Selecionou D4")
						diceCanvas.create_rectangle(dicePos[3][0]+10, dicePos[3][1], dicePos[3][0]+43, dicePos[3][1]+32, outline="#1f1", width = 2)
						finalSeq.remove(seq[3])
# 	Seleciona o dado 5
				if(event.x >= dicePos[4][0] + 10 and event.x <= (dicePos[4][0]+42)):
					if(event.y >= dicePos[4][1] and event.y <= (dicePos[4][1]+32)):
						print("Selecionou D5")
						diceCanvas.create_rectangle(dicePos[4][0]+10, dicePos[4][1], dicePos[4][0]+43, dicePos[4][1]+32, outline="#1f1", width = 2)
						finalSeq.remove(seq[4])

	diceCanvas.bind("<Button-1>", dicesChoice)
	root.mainloop()




# 
# Retorna a sequencia de dados desejada
# 
def getFinalSeq():
	global finalSeq
	return finalSeq


# 
# Carrega os principais elementos para a partida
# 
def loadGameElements(isNewGame): 
	global canvas
	global gameState
	if(isNewGame):
		canvas.delete('confirmNamesTag')
		for i in range(getNumberPlayers()): #Cria o menubar para as tabelas dos jogadores
			entryNames[i].pack_forget()
	else:
		gameState = 2
		canvas.delete('playButtonTag')
		numberOfPlayersEntry.pack_forget()
		question.pack_forget()	
	setUpTableMenubar(root)
	canvas.itemconfigure(tossDicesButton, state = 'normal')
	canvas.coords(tossDicesButton, ((canvas.winfo_width()/2)), 50)
	updateGameStatus()


# 
# Atualiza o status do jogo na interface
# 
def updateGameStatus(): # atualiza na interface a rodada e a vez do jogador\
	turn = getPlayerTurn()
	roundLabel.config(text = 'Rodada número: %d' % (getGameRound()+1))
	playerTurnLabel.config(text = 'Vez do jogador: ' + getPlayerNamesInd(turn))
	roundLabel.pack()
	playerTurnLabel.pack()
	canvas.pack(side = BOTTOM)

# 
# Gerencia as funcoes da interface principal do jogo, desde o seu incio ate o termino da partida
# 
def mainView(): 
	root.title('Yahtzee')
	setNewGame()

#	gameState 0(tela inicial) / 1(entrando os jogadores) / 2(jogo comecou) 
	global gameState
	gameState = 0

# 	Elementos do root
	logoImg = ImageTk.PhotoImage(Image.open("images/yatlogo.png"))
	logo = Label(image = logoImg)
	logo.pack()
	gameFrame = Frame(root)

	global question
	question = Label(text = "Quantos jogadores?", font=('Times', 20))
	question.pack()
	global numberOfPlayersEntry
	numberOfPlayersEntry = Entry(root)
	numberOfPlayersEntry.pack()

	global roundLabel
	global playerTurnLabel
	roundLabel = Label(gameFrame, text = '', font=('Times', 20))
	playerTurnLabel = Label(gameFrame, text = '', font=('Times', 20))

	global canvas
	canvas = Canvas(gameFrame, width=500, height=80, bg='white')  
	gameFrame.pack() 
	canvas.pack(expand=YES, fill=BOTH) 

	global entryNames
	entryNames = [Entry(root), Entry(root), Entry(root), Entry(root), Entry(root), Entry(root)]
	confirmImage = ImageTk.PhotoImage(Image.open("images/confirm.png"))


# 	Menubar com os botoes para salvar e carregar partida
	setUpFileMenubar(root)


# 	Elementos presentes  no canvas
	canvasw = canvas.winfo_width()
	canvash = canvas.winfo_height()

	playImg = ImageTk.PhotoImage(Image.open("images/playimage2.png"))
	playButton = canvas.create_image(250, playImg.height(), image=playImg, anchor=CENTER, tags = 'playButtonTag')
	
	global tossDicesButton
	choiceTossDice = ImageTk.PhotoImage(Image.open("images/tossDices.png"))
	tossDicesButton = canvas.create_image(canvasw/2, 5, image=choiceTossDice, anchor=CENTER, tags = 'tossDicesTag', state = 'hidden')

# 	Guarda as posicoes das imagens que funcionam como botoes
	playImgSize = [playImg.width(), playImg.height()] 
	playImgPos = [canvas.coords('playButtonTag')[0] - playImg.width()/2, canvas.coords('playButtonTag')[1] - playImg.height()/2]
	
	choiceTossDiceSize = [choiceTossDice.width(), choiceTossDice.height()]
	choiceTossDicePos = [canvas.coords('tossDicesTag')[0] - choiceTossDiceSize[0]/2, canvas.coords('tossDicesTag')[1] - choiceTossDiceSize[1]/2]


# 	Evento de clique no canvas
	def beginGameClickEvent(event): # jogador escolhe começar o jogo
		global gameState
		choiceTossDicePos[:] = [canvas.coords('tossDicesTag')[0] - choiceTossDiceSize[0]/2, canvas.coords('tossDicesTag')[1] - choiceTossDiceSize[1]/2]
		if(gameState == 0):
			if(event.x >= playImgPos[0] and event.x <= (playImgPos[0]+playImgSize[0])):
				if(event.y >= playImgPos[1] and event.y <= (playImgPos[1]+playImgSize[1])):
					##SELECIONOU COMECAR O JOGO#####
					gameState = 1
					setNumberPlayers(int(numberOfPlayersEntry.get()))
					beginTables(getNumberPlayers())
					canvas.delete('playButtonTag')
					numberOfPlayersEntry.pack_forget()
					question.pack_forget()	
					for j in range(getNumberPlayers()):
						entryNames[j].pack() #cria os campos para inserir os nomes dos jogadores
					canvas.create_image(canvas.winfo_width()/2, canvas.winfo_height()/2, image=confirmImage, anchor=CENTER, tags='confirmNamesTag')
		elif(gameState == 1):
			confirmImageSize = [confirmImage.width(), confirmImage.height()]
			confirmButtonPos = [canvas.coords('confirmNamesTag')[0]-confirmImageSize[0]/2, canvas.coords('confirmNamesTag')[1]-confirmImageSize[1]/2]
			if(event.x >= confirmButtonPos[0] and event.x <= (confirmButtonPos[0]+confirmImageSize[0])):
				if(event.y >= confirmButtonPos[1] and event.y <= (confirmButtonPos[1]+confirmImageSize[1])):
					for i in range(getNumberPlayers()):
						setPlayerNameInd(entryNames[i].get(), i)
						gameState = 2
					loadGameElements(True)
		else:
			if(getGameRound() >= 13):
				return
			elif(event.x >= choiceTossDicePos[0] and event.x <= (choiceTossDicePos[0]+choiceTossDiceSize[0])):
				if(event.y >= choiceTossDicePos[1] and event.y <= (choiceTossDicePos[1]+choiceTossDiceSize[1])):
					canvas.pack_forget()
					chooseCell(getPlayerTurn(), createSeq())
					status = gameUpdate()
					if(status != None):
						gameFrame.pack_forget()
						winnerLabel = Label(root, text = 'O jogador %d ganhou!' % (status + 1), font=('Times', 20))
						winnerLabel.pack()
						return



	canvas.bind("<Button-1>", beginGameClickEvent) #evento de clique do mouse

	root.mainloop()


