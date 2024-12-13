import json

class FileReader:
    
    def read(path: str, isjson = False):
        with open(path, 'r') as f:
            ret = f.read()
        if isjson: return json.loads(ret)
        return ret

    def readJson(path: str):
        with open(path) as jfile:
            ret = json.load(jfile)
        return ret
    
    def update(path: str, content: str):
        with open(path, "w") as f:
            f.write(content)