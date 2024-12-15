from data.fileManager import FileManager, config, dataPath
from IndoorManageSystem.__types__ import Table, History

from datetime import datetime, timedelta

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
    standardMoist, deviationMoist = conf['standard_moist'], conf['deviation_moist']

    if isInRange(indoorAM, standardMoist, deviationMoist): return 0
    
    if indoorAM > standardMoist: return 1
    else: return 2


def response():
    
    retMessage = {
        'realTimeData': [0,0],
        'control': [tempChecker(), moistChecker()],
        'history': {
            'labels': [], # hours
            'temp': [], # values
            'moist': [], # values
        }
    }
    
    table: Table = FileManager.readJson(dataPath + "/indoor/table.json")
    retMessage['realTimeData'] = [table['temp'][-1], table['moist'][-1]]
    
    history: History = FileManager.readJson(dataPath + "/indoor/history.json")
    
    for i in range(24, 0, -1):
        
        to_date = (datetime.now() - timedelta(hours=i)).strftime("%Y-%m-%d")
        hour = int((datetime.now() - timedelta(hours=i)).strftime("%H"))

        if to_date not in history: continue
        
        for data in history[to_date]:
            if data['hour'] != hour: continue

            retMessage['history']['labels'].append(hour)
            retMessage['history']['temp'].append(data['temp'])
            retMessage['history']['moist'].append(data['moist'])
    
    return retMessage