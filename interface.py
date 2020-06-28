# 
# Nesse modulo constam as funcoes da tela principal do jogo
# 
# 
from tkinter import *
from PIL import ImageTk, Image
from tablemanager import*
from dicemanager import*
from cellmanager import*
from menubar import*
from gamemanager import*
from gameinterface import*
from dicesinterface import*


__all__ = ['mainView', 'displayDices','getFinalSeq','chooseCellEntry']


root = Tk()

# dicesFrame = Frame(root)
# diceCanvas = Canvas(dicesFrame, width=500, height=150, bg='white')

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
					removeGameElements()
					removeDicesElements()
					entryCanvas.pack_forget()
					entryLabel.pack_forget()
					entryFrame.pack_forget()
					# dicesFrame.pack_forget()
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
# Remove elementos iniciais do jogo
# 
def removeStarterViewElements(isNewGame):
	global superFrame
	global canvas
	global gameState
	if(isNewGame):
		canvas.delete('confirmNamesTag')
		namesLabel.pack_forget()
		for i in range(getNumberPlayers()): 
			entryNames[i].pack_forget()
	else:
		gameState = 2
		canvas.delete('playButtonTag')
		numberOfPlayersEntry.pack_forget()
		question.pack_forget()
	superFrame.pack_forget()




# 
# Gerencia as funcoes da interface principal do jogo, desde o seu incio ate o termino da partida
# 
def mainView(): 
	root.title('Yahtzee')
	setNewGame()
	startGameView(root)
	startDiceElements(root)

#	gameState 0(tela inicial) / 1(entrando os jogadores) / 2(jogo comecou) 
	global gameState
	gameState = 0

# 	Elementos do root
	logoImg = ImageTk.PhotoImage(Image.open("images/yatlogo.png"))
	logo = Label(image = logoImg)
	logo.pack()
	# gameFrame = Frame(root)
	global superFrame
	superFrame = Frame(root)

	global question
	question = Label(text = "Quantos jogadores?", font=('Times', 20))
	question.pack()

	global numberOfPlayersEntry
	numberOfPlayersEntry = Entry(root)
	numberOfPlayersEntry.pack()

	global namesLabel
	namesLabel = Label(text = "Qual o nome dos jogadores", font=('Times', 20))


	global canvas
	canvas = Canvas(superFrame, width=500, height=80, bg='white')  
	superFrame.pack() 
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
	

# 	Guarda as posicoes das imagens que funcionam como botoes
	playImgSize = [playImg.width(), playImg.height()] 
	playImgPos = [canvas.coords('playButtonTag')[0] - playImg.width()/2, canvas.coords('playButtonTag')[1] - playImg.height()/2]
	

# 	Evento de clique no canvas
	def beginGameClickEvent(event): # jogador escolhe começar o jogo
		global gameState
		# choiceTossDicePos[:] = [canvas.coords('tossDicesTag')[0] - choiceTossDiceSize[0]/2, canvas.coords('tossDicesTag')[1] - choiceTossDiceSize[1]/2]
#	Jogo ainda nao comecou 
		if(gameState == 0):
#	Selecionou comecar o jogo
			if(event.x >= playImgPos[0] and event.x <= (playImgPos[0]+playImgSize[0])):
				if(event.y >= playImgPos[1] and event.y <= (playImgPos[1]+playImgSize[1])):
					gameState = 1
					setNumberPlayers(int(numberOfPlayersEntry.get()))
					beginTables(getNumberPlayers())
					canvas.delete('playButtonTag')
					numberOfPlayersEntry.pack_forget()
					question.pack_forget()	
					namesLabel.pack(side = TOP)
					for j in range(getNumberPlayers()):
						entryNames[j].pack() #cria os campos para inserir os nomes dos jogadores
					canvas.create_image(canvas.winfo_width()/2, canvas.winfo_height()/2, image=confirmImage, anchor=CENTER, tags='confirmNamesTag')
					superFrame.pack(side = BOTTOM)
# 	Usuario comecaram a colocar seus nomes
		elif(gameState == 1):
			confirmImageSize = [confirmImage.width(), confirmImage.height()]
			confirmButtonPos = [canvas.coords('confirmNamesTag')[0]-confirmImageSize[0]/2, canvas.coords('confirmNamesTag')[1]-confirmImageSize[1]/2]
# 	Usuarios confirmam seus nomes
			if(event.x >= confirmButtonPos[0] and event.x <= (confirmButtonPos[0]+confirmImageSize[0])):
				if(event.y >= confirmButtonPos[1] and event.y <= (confirmButtonPos[1]+confirmImageSize[1])):
					for i in range(getNumberPlayers()):
						setPlayerNameInd(entryNames[i].get(), i)
						gameState = 2
					loadGameElements(True)



	canvas.bind("<Button-1>", beginGameClickEvent) #evento de clique do mouse

	root.mainloop()




