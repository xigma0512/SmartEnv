from data.fileManager import FileManager, config, dataPath
from OutdoorManageSystem.__types__ import Table, History

from datetime import datetime, timedelta

def response():
    
    retMessage = {
        'realTimeData': [0,0,0],
        'history': {
            'labels': [], # hours
            'temp': [], # values
            'moist': [], # values
            'PM25': [] # values
        }   
    }

    table: Table = FileManager.readJson(dataPath + "/outdoor/table.json")
    retMessage['realTimeData'] = [table['temp'][-1], table['moist'][-1], table['PM25'][-1]]
    
    history: History = FileManager.readJson(dataPath + "/outdoor/history.json")
    
    for i in range(24, 0, -1):
        
        to_date = (datetime.now() - timedelta(hours=i)).strftime("%Y-%m-%d")
        hour = int((datetime.now() - timedelta(hours=i)).strftime("%H"))

        if to_date not in history: continue
        
        for data in history[to_date]:
            if data['hour'] != hour: continue

            retMessage['history']['labels'].append(hour)
            retMessage['history']['temp'].append(data['temp'])
            retMessage['history']['moist'].append(data['moist'])
            retMessage['history']['PM25'].append(data['PM25'])
    
    return retMessage