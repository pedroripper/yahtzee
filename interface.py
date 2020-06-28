from tkinter import *
from PIL import ImageTk, Image
from tablemanager import*
from dice import*
from chooseCell import*
from menubar import*
from gamemanager import*


__all__ = ['mainView', 'displayDices','finalSeq','chooseCellEntry']


root = Tk()

isShowingCellChoice = [False]
isEditingDices = [False]
finalSeq = []
gameStarted = [0]
selectedCell = []
dicesFrame = Frame(root)
diceCanvas = Canvas(dicesFrame, width=500, height=150, bg='white')
chancesLabel = Label(dicesFrame, text = "Chances: %d" % 0,  font=('Times', 20), compound = "center")

# 
# Escolhe a celula que deseja inserir na interface
# 
def chooseCellEntry(dCelulas): 
	entryFrame = Frame(root)
	entryFrame.pack()
	isShowingCellChoice[0] = True
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
		confirmImageSize = [confirmImage.width(), confirmImage.height()]
		confirmButtonPos = [entryCanvas.coords('checkCellButton')[0]-confirmImageSize[0]/2, entryCanvas.coords('checkCellButton')[1]-confirmImageSize[1]/2]
		
		if(event.x >= confirmButtonPos[0] and event.x <= (confirmButtonPos[0]+confirmImageSize[0])):
				if(event.y >= confirmButtonPos[1] and event.y <= (confirmButtonPos[1]+confirmImageSize[1])):
					selectedCell[:] = [entry.get()]
					entryCanvas.pack_forget()
					entryLabel.pack_forget()
					entryFrame.pack_forget()
					root.quit()
	entryCanvas.bind("<Button-1>", cellChoice)
	root.mainloop()


# 
# Exibe os dados lancados pelo usuario para escolher quais lancar novamenrte
# 
def displayDices(seq, chances): 
	
	global diceFrame    
	global diceCanvas
	global chancesLabel

	dicesFrame.pack()
	chancesLabel = Label(dicesFrame, text = "Chances: %d" % chances,  font=('Times', 20), compound = "center")
	if(chances < 2): #Se ja jogou uma vez limpa av view para exibir de novo
		diceCanvas.delete("all")
		chancesLabel.pack_forget()
		diceCanvas.pack_forget()

	canvasw = diceCanvas.winfo_width()
	canvash = diceCanvas.winfo_height()
	diceImages = [] #imagens dos dados colocadas no canvas
	dicePos = [[],[],[],[],[]] #posicao de cada um dos 5 dados


	diceCanvas.pack(expand=YES, fill=BOTH) 

	changeDicesLabel = Label(dicesFrame, text = "Você deseja mudar seus dados?",  font=('Times', 20), compound = "center")


	startedSelectingDices = [False]

# 
# 	Imagem dos dados
# 
	dice1Image = ImageTk.PhotoImage(Image.open("images/dado_1.png"))
	dice2Image = ImageTk.PhotoImage(Image.open("images/dado_2.png"))
	dice3Image = ImageTk.PhotoImage(Image.open("images/dado_3.png"))
	dice4Image = ImageTk.PhotoImage(Image.open("images/dado_4.png"))
	dice5Image = ImageTk.PhotoImage(Image.open("images/dado_5.png"))
	dice6Image = ImageTk.PhotoImage(Image.open("images/dado_6.png"))

	diceSize =  [dice1Image.width(), dice1Image.height()] #dimensao dos dados

	finalSeq[:] = seq


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

	maintainimage = ImageTk.PhotoImage(Image.open("images/confirm.png"))
	changeImage = ImageTk.PhotoImage(Image.open("images/changedices.png"))
	maintainButton = diceCanvas.create_image((250-5) - (maintainimage.width()/2), 120, image=maintainimage, anchor=CENTER, tags = 'maintainButtonTag')
	changeButton = diceCanvas.create_image((250+5) + (changeImage.width()/2), 120, image=changeImage, anchor=CENTER, tags = 'changeButtonTag')
	tossAgainImage = ImageTk.PhotoImage(Image.open("images/tossAgain.png"))
	tossAgainButton = diceCanvas.create_image((250), 120, image=tossAgainImage, anchor=CENTER, tags = 'tossAgainButtonTag', state = 'hidden')
	
	maintainButtonSize = [maintainimage.width(), maintainimage.height()]
	maintainButtonPos = [diceCanvas.coords('maintainButtonTag')[0] - maintainButtonSize[0]/2, diceCanvas.coords('maintainButtonTag')[1] - maintainButtonSize[1]/2]

	changeButtonSize = [changeImage.width(), changeImage.height()]
	changeButtonPos = [diceCanvas.coords('changeButtonTag')[0] - changeButtonSize[0]/2, diceCanvas.coords('changeButtonTag')[1] - changeButtonSize[1]/2]

	tossAgainButtonSize = [tossAgainImage.width(), tossAgainImage.height()]
	tossAgainButtonPos = [diceCanvas.coords('tossAgainButtonTag')[0] - tossAgainButtonSize[0]/2, diceCanvas.coords('tossAgainButtonTag')[1] - tossAgainButtonSize[1]/2]
	
	if(chances == 0):
		diceCanvas.itemconfigure(maintainButton, state = 'hidden')
		diceCanvas.itemconfigure(changeButton, state = 'hidden')
		maintainimage = ImageTk.PhotoImage(Image.open("images/confirm.png"))
		confirmButton = diceCanvas.create_image((250), 120, image=maintainimage, anchor=CENTER, tags = 'confirmButtonTag')
		confirmButtonSize = [maintainimage.width(), maintainimage.height()]
		confirmButtonPos = [diceCanvas.coords('confirmButtonTag')[0] - confirmButtonSize[0]/2, diceCanvas.coords('confirmButtonTag')[1] - confirmButtonSize[1]/2]

# 
# 	Decisoes sobre os dados
# 
	def dicesChoice(event):
		global diceCanvas
		if(chances == 0):
			if(event.x >= confirmButtonPos[0] and event.x <= (confirmButtonPos[0]+confirmButtonSize[0])):
				if(event.y >= confirmButtonPos[1] and event.y <= (confirmButtonPos[1]+confirmButtonSize[1])):
					print("Essa parte ta repetindo")
					dicesFrame.pack_forget()
					root.quit()
		else:
			if(startedSelectingDices[0] == 0):
				if(event.x >= maintainButtonPos[0] and event.x <= (maintainButtonPos[0]+maintainButtonSize[0])):
					if(event.y >= maintainButtonPos[1] and event.y <= (maintainButtonPos[1]+maintainButtonSize[1])): 
						dicesFrame.pack_forget()
						root.quit()
						##MANTER OS DADOS
				if(event.x >= changeButtonPos[0] and event.x <= (changeButtonPos[0]+changeButtonSize[0])):
					if(event.y >= changeButtonPos[1] and event.y <= (changeButtonPos[1]+changeButtonSize[1])):
						diceCanvas.itemconfigure(tossAgainButton, state = 'normal')
						diceCanvas.itemconfigure(maintainButton, state = 'hidden')
						diceCanvas.itemconfigure(changeButton, state = 'hidden')
						startedSelectingDices[0] = 1
			if(startedSelectingDices[0] == 1):
				if(event.x >= tossAgainButtonPos[0] and event.x <= (tossAgainButtonPos[0]+tossAgainButtonSize[0])):
					if(event.y >= tossAgainButtonPos[1] and event.y <= (tossAgainButtonPos[1]+tossAgainButtonSize[1])):
						startedSelectingDices[0] = 2
						root.quit()
						#ENVIA
				if(event.x >= dicePos[0][0] + 10 and event.x <= (dicePos[0][0]+42)):
					if(event.y >= dicePos[0][1] and event.y <= (dicePos[0][1]+32)):
						print("Selecionou D1")
						diceCanvas.create_rectangle(dicePos[0][0]+10, dicePos[0][1], dicePos[0][0]+43, dicePos[0][1]+32, outline="#1f1", width = 2)
						finalSeq.remove(seq[0])
				if(event.x >= dicePos[1][0] + 10 and event.x <= (dicePos[1][0]+42)):
					if(event.y >= dicePos[1][1] and event.y <= (dicePos[1][1]+32)):
						print("Selecionou D2")
						diceCanvas.create_rectangle(dicePos[1][0]+10, dicePos[1][1], dicePos[1][0]+43, dicePos[1][1]+32, outline="#1f1", width = 2)
						finalSeq.remove(seq[1])
				if(event.x >= dicePos[2][0] + 10 and event.x <= (dicePos[2][0]+42)):
					if(event.y >= dicePos[2][1] and event.y <= (dicePos[2][1]+32)):
						print("Selecionou D3")
						diceCanvas.create_rectangle(dicePos[2][0]+10, dicePos[2][1], dicePos[2][0]+43, dicePos[2][1]+32, outline="#1f1", width = 2)
						finalSeq.remove(seq[2])
				if(event.x >= dicePos[3][0] + 10 and event.x <= (dicePos[3][0]+42)):
					if(event.y >= dicePos[3][1] and event.y <= (dicePos[3][1]+32)):
						print("Selecionou D4")
						diceCanvas.create_rectangle(dicePos[3][0]+10, dicePos[3][1], dicePos[3][0]+43, dicePos[3][1]+32, outline="#1f1", width = 2)
						finalSeq.remove(seq[3])
				if(event.x >= dicePos[4][0] + 10 and event.x <= (dicePos[4][0]+42)):
					if(event.y >= dicePos[4][1] and event.y <= (dicePos[4][1]+32)):
						print("Selecionou D5")
						diceCanvas.create_rectangle(dicePos[4][0]+10, dicePos[4][1], dicePos[4][0]+43, dicePos[4][1]+32, outline="#1f1", width = 2)
						finalSeq.remove(seq[4])




	diceCanvas.bind("<Button-1>", dicesChoice)
	root.mainloop()




# 
# Carrega os principais elementos para a partida
# 
def loadGameElements(isNewGame): 
	global canvas
	if(isNewGame):
		canvas.delete('confirmNamesTag')
		for i in range(getNumberPlayers()): #Cria o menubar para as tabelas dos jogadores
			entryNames[i].pack_forget()
	else:
		gameStarted[0] = 2
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


# 	
# 	Elementos do root
# 
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


# 
# 	Menubar com os botoes para salvar e carregar partida
# 
	setUpFileMenubar(root)

	# gameMenu = Menu(menubar, tearoff = False)
	# gameMenu.add_command(label="Carregar", command=loadGame)
	# gameMenu.add_command(label="Salvar", command=lambda : saveGame(numPlayers[0], nplayerTurn[0], gameRound[0]))
	# menubar.add_cascade(menu = gameMenu, label = "Partida")

# 
# 	Elementos presentes  no canvas
# 
	canvasw = canvas.winfo_width()
	canvash = canvas.winfo_height()

	playImg = ImageTk.PhotoImage(Image.open("images/playimage2.png"))
	playButton = canvas.create_image(250, playImg.height(), image=playImg, anchor=CENTER, tags = 'playButtonTag')
	
	global tossDicesButton
	choiceTossDice = ImageTk.PhotoImage(Image.open("images/tossDices.png"))
	tossDicesButton = canvas.create_image(canvasw/2, 5, image=choiceTossDice, anchor=CENTER, tags = 'tossDicesTag', state = 'hidden')

# 
# 	Guarda as posicoes das imagens que funcionam como botoes
# 
	playImgSize = [playImg.width(), playImg.height()] 
	playImgPos = [canvas.coords('playButtonTag')[0] - playImg.width()/2, canvas.coords('playButtonTag')[1] - playImg.height()/2]
	
	choiceTossDiceSize = [choiceTossDice.width(), choiceTossDice.height()]
	choiceTossDicePos = [canvas.coords('tossDicesTag')[0] - choiceTossDiceSize[0]/2, canvas.coords('tossDicesTag')[1] - choiceTossDiceSize[1]/2]



	def beginGameClickEvent(event): # jogador escolhe começar o jogo
		choiceTossDicePos[:] = [canvas.coords('tossDicesTag')[0] - choiceTossDiceSize[0]/2, canvas.coords('tossDicesTag')[1] - choiceTossDiceSize[1]/2]
		if(gameStarted[0] == 0):
			if(event.x >= playImgPos[0] and event.x <= (playImgPos[0]+playImgSize[0])):
				if(event.y >= playImgPos[1] and event.y <= (playImgPos[1]+playImgSize[1])):
					##SELECIONOU COMECAR O JOGO#####
					gameStarted[0] = 1
					setNumberPlayers(int(numberOfPlayersEntry.get()))
					# print(getNumberPlayers())
					beginTables(getNumberPlayers())
					canvas.delete('playButtonTag')
					numberOfPlayersEntry.pack_forget()
					question.pack_forget()	
					for j in range(getNumberPlayers()):
						entryNames[j].pack() #cria os campos para inserir os nomes dos jogadores
					canvas.create_image(canvas.winfo_width()/2, canvas.winfo_height()/2, image=confirmImage, anchor=CENTER, tags='confirmNamesTag')
		elif(gameStarted[0] == 1):
			confirmImageSize = [confirmImage.width(), confirmImage.height()]
			confirmButtonPos = [canvas.coords('confirmNamesTag')[0]-confirmImageSize[0]/2, canvas.coords('confirmNamesTag')[1]-confirmImageSize[1]/2]
			if(event.x >= confirmButtonPos[0] and event.x <= (confirmButtonPos[0]+confirmImageSize[0])):
				if(event.y >= confirmButtonPos[1] and event.y <= (confirmButtonPos[1]+confirmImageSize[1])):
					for i in range(getNumberPlayers()):
						setPlayerNameInd(entryNames[i].get(), i)
						gameStarted[0] = 2
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


