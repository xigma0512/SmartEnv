import json
import os

class FileManager:
    
    def read(path: str):
        with open(path, 'r') as file:
            ret = file.read()
        return ret
    
    def update(path: str, content: str):
        with open(path, "w") as file:
            file.write(content)
            
    def readJson(path: str):
        with open(path) as jfile:
            ret = json.load(jfile)
        return ret
            
    def updateJson(path: str, content: str):
        with open(path, "w") as jfile:
            json.dump(content, jfile)


dataPath = os.path.dirname(__file__)
config = FileManager.readJson(os.path.dirname(__file__) + "/config.json")
