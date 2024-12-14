from datetime import datetime, timedelta
from IndoorManageSystem.__types__ import DataType, Table, History
from data.fileManager import FileManager, dataPath
    
def record(data: DataType):
    try:
        dt = datetime.fromtimestamp(data['timestamp'])
        to_date = dt.strftime("%Y-%m-%d")
        
        tablePath = dataPath + "/indoor/table.json"
        historyPath = dataPath + "/indoor/history.json"
        
        table: Table = FileManager.readJson(tablePath)
        history: History = FileManager.readJson(historyPath)

        if to_date not in history: 
            history[to_date] = []
            lastUpdate = history[dt - timedelta(days=1)][-1]
        else:
            lastUpdate = history[to_date][-1]
            
        if dt.hour != lastUpdate['hour']:
            history[to_date].append({
                "hour": dt.hour,
                "temp": sum(table['temp']) / len(table['temp']),
                "moist": sum(table['moist']) / len(table['moist'])
            })
            FileManager.updateJson(historyPath, history)
    
            table['temp'].clear()
            table['moist'].clear()
            FileManager.updateJson(tablePath, table)

        table['temp'].append(data['temp'])
        table['moist'].append(data['moist'])
        FileManager.updateJson(tablePath, table)
        return True, None
    
    except Exception as exception:
        return False, exception