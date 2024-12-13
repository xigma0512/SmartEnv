from fileReader import FileReader
from IndoorManageSystem.__types__ import TableType

import os

currentDir = os.path.dirname(__file__)

def isInRange(value: float, standard: float, deviation: float):
    return abs(value - standard) <= deviation

# return [0: 什麼都不做, 1: 開窗, 2: 開冷氣, 3: 開暖氣, 4: Error]
def tempChecker():
    
    indoorTable: TableType = FileReader.read(currentDir + "/table/indoorTable.txt", True)
    outdoorTable: TableType = FileReader.read(currentDir + "/table/outdoorTable.txt", True)
    conf = FileReader.readJson(os.path.dirname(currentDir) + "/config.json")['indoorManageSystem']
    
    indoorAT = indoorTable['averageTemp']
    outdoorAT = outdoorTable['averageTemp']
    standardTemp = conf['standard_temp']
    deviationTemp = conf['deviation_temp']
    
    if isInRange(indoorAT, standardTemp, deviationTemp): return 0
    
    if isInRange(outdoorAT, standardTemp, deviationTemp): return 1
    if indoorAT > standardTemp:
        if outdoorAT < standardTemp: return 1
        return 2
    else:        
        if outdoorAT > standardTemp: return 1
        return 3

# return [0: 什麼都不做, 1: 開啟除濕機, 2: 開啟加濕器]
def moistChecker():
    
    indoorTable: TableType = FileReader.read(currentDir + "/table/indoorTable.txt", True)
    conf = FileReader.readJson(os.path.dirname(currentDir) + "/config.json")['indoorManageSystem']
    
    indoorAM = indoorTable['averageMoist']
    standardMoist = conf['standard_moist']
    deviationMoist = conf['deviation_moist']

    if isInRange(indoorAM, standardMoist, deviationMoist): return 0
    
    if indoorAM > standardMoist: return 1
    else: return 2

def response():
    
    retMessage = {
        'control': [False for i in range(5)],
        'value': [0,0]
    }
    
    tempResult = tempChecker()
    moistResult = moistChecker()
    if tempResult != 0: retMessage['control'][tempResult - 1] = True
    if moistResult != 0: retMessage['control'][moistResult - 1] = True
    
    indoorTable: TableType = FileReader.read(currentDir + "/table/indoorTable.txt", True)
    retMessage['value'] = [indoorTable['averageTemp'], indoorTable['averageMoist']]
    
    return retMessage

response()