from data.fileManager import FileManager, config, dataPath
from IndoorManageSystem.__types__ import Table, History

from datetime import datetime

def isInRange(value: float, standard: float, deviation: float):
    return abs(value - standard) <= deviation

# return [0: 什麼都不做, 1: 開窗, 2: 開冷氣, 3: 開暖氣, 4: Error]
def tempChecker():
    
    to_date = datetime.now().strftime("%Y-%m-%d")
    
    indoorHistory: History = FileManager.readJson(dataPath + "/indoor/history.json")
    outdoorHistory: History = FileManager.readJson(dataPath + "/outdoor/history.json")
    conf = config['indoorManageSystem']
    
    indoorAT, outdoorAT = indoorHistory[to_date][-1]['temp'], outdoorHistory[to_date][-1]['temp']
    standardTemp, deviationTemp = conf['standard_temp'], conf['deviation_temp']
    
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
    
    to_date = datetime.now().strftime("%Y-%m-%d")
    
    indoorHistory: History = FileManager.readJson(dataPath + "/indoor/history.json")
    conf = config['indoorManageSystem']
    
    indoorAM = indoorHistory[to_date][-1]['moist']
    standardMoist, deviationMoist = conf['standard_temp'], conf['deviation_temp']

    if isInRange(indoorAM, standardMoist, deviationMoist): return 0
    
    if indoorAM > standardMoist: return 1
    else: return 2


def response():
    
    retMessage = {
        'control': [False for i in range(5)],
        'realTimeData': [0,0],
        'latestHistory': None    
    }
    
    tempResult = tempChecker()
    moistResult = moistChecker()
    if tempResult != 0: retMessage['control'][tempResult - 1] = True
    if moistResult != 0: retMessage['control'][moistResult - 1] = True
    
    history: History = FileManager.readJson(dataPath + "/indoor/history.json")
    table: Table = FileManager.readJson(dataPath + "/indoor/table.json")
    
    to_date = datetime.now().strftime("%Y-%m-%d")
    
    retMessage['realTimeData'] = [table['temp'][-1], table['moist'][-1]]
    retMessage['latestHistory'] = history[to_date][-1] 
    
    return retMessage