# 
# Nesse modulo constam as funcoes responsaveis por administrar a partida do jogo
# e tambem os nomes dos participantes
# 

import interface as inter
import tablemanager as tm


__all__ = ['getNumberPlayers', 'setNumberPlayers','getPlayerNames','setPlayerNames','setPlayerNameInd','getPlayerTurn','setPlayerTurn','getGameRound','setGameRound','setNewGame','gameUpdate','getPlayerNamesInd']


# 
# Altera o numero de jogadores com jogo carregado
# 
def setNumberPlayers(number):
	global numPlayers
	numPlayers = number


# 
# Renorna o numero de jogadores
# 
def getNumberPlayers():
	global numPlayers
	return numPlayers


# 
# Renorna o nome dos jogadores
# 
def getPlayerNames():
	global PlayerNameList
	return PlayerNameList

# 
# Renorna o nome de um jogador
# 
def getPlayerNamesInd(player):
	global PlayerNameList
	return PlayerNameList[player]


# 
# Altera o nome dos jogadores com jogo carregado
# 
def setPlayerNames(nameList):
	global PlayerNameList
	PlayerNameList[:(numPlayers-1)] = nameList.split()

# 
# Altera o nome de um jogador
# 
def setPlayerNameInd(name, nPlayer):
	global PlayerNameList
	PlayerNameList[nPlayer] +=  name
# 
# Renorna a vez do jogador x
# 
def getPlayerTurn():
	global nplayerTurn
	return nplayerTurn

# 
# Altera a vez do jogador x com jogo carregado
# 
def setPlayerTurn(turn):
	global nplayerTurn
	nplayerTurn = turn

# 
# Renorna rodada da partida
# 
def getGameRound():
	global gameRound
	return gameRound

# 
# Renorna rodada da partida com jogo alterado
# 
def setGameRound(loadedRound):
	global gameRound
	gameRound = loadedRound

# 
# Inicio do jogo. Dados iniciais dos jogadores
# 
def setNewGame():
	global PlayerNameList
	global gameRound
	global nplayerTurn
	global numPlayers
	PlayerNameList = ['','','','','','']
	gameRound = 0
	nplayerTurn = 0
	numPlayers = 0


# 
# Calcula o vencedor do jogo e retorna o indice do ganhador
# 
def calcWinner():
	global numPlayers
	winnerIndex = 0
	score = 0
	highscore = 0
	# print("Fim do jogo!\n")
	# print("Pontuacoes:\n")
	for i in range(numPlayers):
		score = tm.calcTable(i)
		# print("Jogador " + str(i+1) +": " + str(score) + "pontos\n")
		if score > highscore:
			highscore = score
			winnerIndex = i
	return winnerIndex

# 
# Atualiza a partida com as vezes dos jogadores e rodada
# returna o status do jogo None(Continua) Int(indice do ganhador)
def gameUpdate():
	global nplayerTurn
	global gameRound
	if(nplayerTurn == numPlayers-1):
		gameRound += 1
		nplayerTurn = 0
		if(gameRound == 13):
			return calcWinner()
	else:
		nplayerTurn += 1
	inter.updateGameStatus()
	return None






