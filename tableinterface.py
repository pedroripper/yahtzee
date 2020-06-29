# 
# Nesse modulo consta a funcao de exibir a interface da tabela do jogador
# em uma janela secundaria
# 

from tkinter import *
from PIL import ImageTk, Image
from gamemanager import *
import interface as inter


__all__ = ['displayTable']


# 
# Exibe a tabela do usuario
# 
def displayTable(table, nplayer):
	tableWindow = Toplevel()
	tableFrame = Frame(tableWindow)
	playerLabel = Label(tableWindow,  text = "Tabela de " + getPlayerNamesInd(nplayer),font=('Times', 20), compound = "center")
	playerLabel.pack()

	imgOne = ImageTk.PhotoImage(Image.open("images/umCell.png"))
	imgTwo = ImageTk.PhotoImage(Image.open("images/doisCell.png"))
	imgThree = ImageTk.PhotoImage(Image.open("images/tresCell.png"))
	imgFour = ImageTk.PhotoImage(Image.open("images/quatroCell.png"))
	imgFive = ImageTk.PhotoImage(Image.open("images/cincoCell.png"))
	imgSix = ImageTk.PhotoImage(Image.open("images/seisCell.png"))
	imgT = ImageTk.PhotoImage(Image.open("images/trincaCell.png"))
	imgQ = ImageTk.PhotoImage(Image.open("images/quadraCell.png"))
	imgFH = ImageTk.PhotoImage(Image.open("images/fullHouseCell.png"))
	imgSeqMax = ImageTk.PhotoImage(Image.open("images/seqmaxCell.png"))
	imgSeqMin = ImageTk.PhotoImage(Image.open("images/seqminCell.png"))
	imgYah = ImageTk.PhotoImage(Image.open("images/yCell.png"))
	imgChance = ImageTk.PhotoImage(Image.open("images/chanceCell.png"))
	imgBonus = ImageTk.PhotoImage(Image.open("images/yBCell.png"))
	imgBlank = ImageTk.PhotoImage(Image.open("images/blankCell.png"))

	frame1 = Frame(tableFrame)
	frame2 = Frame(tableFrame)
	frame3 = Frame(tableFrame)
	frame4 = Frame(tableFrame)
	frame5 = Frame(tableFrame)
	frame6 = Frame(tableFrame)
	frame7 = Frame(tableFrame)

	onesLabel = Label(frame1, image = imgOne)
	twosLabel = Label(frame2, image = imgTwo)
	threesLabel = Label(frame3, image = imgThree)
	foursLabel = Label(frame4, image = imgFour)
	fivesLabel = Label(frame5, image = imgFive)
	sixesLabel = Label(frame6, image = imgSix)
	tricLabel = Label(frame7, image = imgT)
	quadLabel = Label(frame1,image = imgQ)
	fhLabel = Label(frame2, image = imgFH)
	seqMaxLabel = Label(frame4, image = imgSeqMax)
	seqMinLabel = Label(frame3, image = imgSeqMin)
	yahLabel = Label(frame5, image = imgYah)
	chanceLabel = Label(frame6, image = imgChance)
	bonusLabel = Label(frame7, image = imgBonus)

	blankLabel1 = Label(frame1, image = imgBlank, text = "%s" % table[0],  font=('Times', 20), compound = "center")
	blankLabel2 = Label(frame2, image = imgBlank, text = "%s" % table[1],  font=('Times', 20), compound = "center")
	blankLabel3 = Label(frame3, image = imgBlank, text = "%s" % table[2],  font=('Times', 20), compound = "center")
	blankLabel4 = Label(frame4, image = imgBlank, text = "%s" % table[3],  font=('Times', 20), compound = "center")
	blankLabel5 = Label(frame5, image = imgBlank, text = "%s" % table[4],  font=('Times', 20), compound = "center")
	blankLabel6 = Label(frame6, image = imgBlank, text = "%s" % table[5],  font=('Times', 20), compound = "center")
	blankLabel7 = Label(frame7, image = imgBlank, text = "%s" % table[6],  font=('Times', 20), compound = "center")
	blankLabel8 = Label(frame1, image = imgBlank, text = "%s" % table[7],  font=('Times', 20), compound = "center")
	blankLabel9 = Label(frame2, image = imgBlank, text = "%s" % table[8],  font=('Times', 20), compound = "center")
	blankLabel10 = Label(frame3, image = imgBlank, text = "%s" % table[9],  font=('Times', 20), compound = "center")
	blankLabel11 = Label(frame4, image = imgBlank, text = "%s" % table[10],  font=('Times', 20), compound = "center")
	blankLabel12 = Label(frame5, image = imgBlank, text = "%s" % table[11],  font=('Times', 20), compound = "center")
	blankLabel13 = Label(frame6, image = imgBlank, text = "%s" % table[12],  font=('Times', 20), compound = "center")
	blankLabel14 = Label(frame7, image = imgBlank, text = "%s" % table[13],  font=('Times', 20), compound = "center")


	tableFrame.pack(side = BOTTOM)
	frame1.pack()
	onesLabel.pack(side = LEFT)
	blankLabel1.pack(side = LEFT)
	quadLabel.pack(side = LEFT)
	blankLabel8.pack(side = LEFT)

	frame2.pack()
	twosLabel.pack(side = LEFT)
	blankLabel2.pack(side = LEFT)
	fhLabel.pack(side = LEFT)
	blankLabel9.pack(side = LEFT)

	frame3.pack()
	threesLabel.pack(side = LEFT)
	blankLabel3.pack(side = LEFT)
	seqMinLabel.pack(side = LEFT)
	blankLabel10.pack(side =LEFT)

	frame4.pack()
	foursLabel.pack(side = LEFT)
	blankLabel4.pack(side = LEFT)
	seqMaxLabel.pack(side = LEFT)
	blankLabel11.pack(side = LEFT)

	frame5.pack()
	fivesLabel.pack(side = LEFT)
	blankLabel5.pack(side = LEFT)
	yahLabel.pack(side = LEFT)
	blankLabel12.pack(side = LEFT)

	frame6.pack()
	sixesLabel.pack(side = LEFT)
	blankLabel6.pack(side = LEFT)
	chanceLabel.pack(side = LEFT)
	blankLabel13.pack(side = LEFT)

	frame7.pack()
	tricLabel.pack(side = LEFT)
	blankLabel7.pack(side = LEFT)
	bonusLabel.pack(side = LEFT)
	blankLabel14.pack(side = LEFT)

	inter.root.mainloop()