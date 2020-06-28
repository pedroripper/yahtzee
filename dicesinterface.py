
# 
# Exibe os dados lancados pelo usuario para escolher quais lancar novamenrte
# 
def displayDices(seq, chances): 
	
	global diceFrame    
	global diceCanvas
	global finalSeq

	dicesFrame.pack(side= BOTTOM)

# 	Se ja jogou uma vez limpa av view para exibir de novo
	if(chances < 2): 
		diceCanvas.delete("all")
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

