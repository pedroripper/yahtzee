# 
# Nesse modulo constam as funcoes responsaveis pelas operacoes nas tabelas dos jogadores
# 
# 

import tableinterface as ti
__all__ = ['beginTables', 'insertValue', 'calcTable','getUserTable','getSampleTable','loadTable','prepareTableToSave']


tables = []

# 
# Inicializa a tabela de acordo com o numero de jogadores
# 
def beginTables(nPlayers):
        if tables != [] or  not isinstance(nPlayers,int) or nPlayers < 1:
                return False
        for i in range(0,nPlayers):
                tables[:] += [['0','0','0','0','0','0','0','0','0','0','0','0','0','0']]
        return True
# 
# Prepara a tabela de um usuario para string para ser salva no txt
# 
def prepareTableToSave(nPlayer):
        tableLst = ""
        for i in tables[nPlayer]:
                tableLst += str(i) + " "
        return tableLst

# 
# Atualiza a tabela com a de um jogo anterior
# 
def loadTable(loadedTable):
        tables[:] = loadedTable

# 
# Insere valor na tabela
# 
def insertValue(nPlayer,cel,value):
        if not value:
                return False
        if cel == 13:
                if(str(tables[nPlayer][11]) != '0'):
                        return False
                else:
                        tables[nPlayer][cel] = str(int(tables[nPlayer][cel]) + value)
                        return True
        elif(tables[nPlayer][cel] != '0'):
                return False
        else:
                tables[nPlayer][cel] = str(value)
                print('Insercao concluida!')
                return True

# 
# Calcula valor total da tabela de um usuario
# 
def calcTable(nPlayer):
        totalUpper = 0
        for cel in range(0,6):
                totalUpper += int(tables[nPlayer][cel])
        totalLower = 0
        for cel in range(6,14):
                totalLower += int(tables[nPlayer][cel])
        if totalLower > 62:
                totalLower += 35

        return (totalUpper+totalLower)

def getSampleTable(dCelulas):
        it.displayTable(dCelulas)
        return

# 
# Retorna a tabela de um usuario
# 
def getUserTable(nPlayer):
        print("\nSua tabela:\n")
        t = tables[nPlayer]
        ti.displayTable(t, nPlayer)
        return
