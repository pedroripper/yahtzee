# 
# Nesse modulo constam as funcoes da interface relacionadas
# a insercao nas celulas
# 

from tkinter import *
from PIL import ImageTk, Image
import dicesinterface as di
import gameinterface as gi
__all__ = ['startCellElements','chooseCellEntry']

global entryFrame

# 
# Inicializa os elementos
# 
def startCellElements(root):
	global entryFrame
	global mainRoot
	mainRoot = root
	entryFrame = Frame(mainRoot)

# 
# Escolhe a celula que deseja inserir na interface
# 
def chooseCellEntry(dCelulas): 
	global entryFrame
	global mainRoot
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
		global mainRoot
		global entryFrame
		global selectedCell
		global dicesFrame
		selectedCell = ""
		confirmImageSize = [confirmImage.width(), confirmImage.height()]
		confirmButtonPos = [entryCanvas.coords('checkCellButton')[0]-confirmImageSize[0]/2, entryCanvas.coords('checkCellButton')[1]-confirmImageSize[1]/2]
		if(event.x >= confirmButtonPos[0] and event.x <= (confirmButtonPos[0]+confirmImageSize[0])):
				if(event.y >= confirmButtonPos[1] and event.y <= (confirmButtonPos[1]+confirmImageSize[1])):
					selectedCell += entry.get()
					gi.removeGameElements()
					di.removeDicesElements()
					entryCanvas.pack_forget()
					entryLabel.pack_forget()
					entryFrame.pack_forget()
					entry.pack_forget()
					# dicesFrame.pack_forget()
					mainRoot.quit()
	entryCanvas.bind("<Button-1>", cellChoice)
	mainRoot.mainloop()

# 
# Retorna a celula que o jogador deseja preencher
# 
def getSelectedCell():
	global selectedCell
	return selectedCell

