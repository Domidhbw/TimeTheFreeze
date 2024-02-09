import json


class SaveManager():
    def __init__(self) -> None:
        self.file = './saveFile.json'
        self.data = 0
        self.levelVar = 0
        self.readJson()

    def writeCurrentLevel(self,level):
        self.data['LevelsDone'] = level

    def readJson(self):
        with open(self.file,'r') as saveFile:
            self.data = json.load(saveFile)
            self.levelVar = self.data['LevelsDone']

    def writeJson(self):
        with open(self.file, 'w') as file:
            json.dump(self.data, file, indent=4)