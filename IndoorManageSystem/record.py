from datetime import datetime
from IndoorManageSystem.__types__ import DataType, TableType
from fileReader import FileReader

import os
import json

currentDir = os.path.dirname(__file__)

def record(data: DataType):
    try:
        dt = datetime.fromtimestamp(data['timestamp'])
        tablePath = currentDir + "/table/" + data['mode'] + 'Table.txt'

        table: TableType = FileReader.read(tablePath, True)

        if dt.minute != 0:
            table['temp'].append(data['temp'])
            table['moist'].append(data['moist'])
            FileReader.update(tablePath, json.dumps(table))
            return True, None

        table['averageTemp'] = sum(table['temp']) / len(table['temp']) if table['temp'] else 0
        table['averageMoist'] = sum(table['moist']) / len(table['moist']) if table['moist'] else 0
        table['temp'].clear()
        table['moist'].clear()
        FileReader.update(tablePath, json.dumps(table))
        return True, None
    except Exception as e:
        return False, e