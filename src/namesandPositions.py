

class NamesandPositions():
    def __init__(self, namesPos:dict):
        self._dictionary = namesPos
        self._values = tuple(self._dictionary.values())
        self._keys = tuple(self._dictionary.keys())
        self._length = len(self._values)

    def showDictionary(self):
        return self._dictionary
    

    def showPos(self, valuePos:int=None):
        if valuePos == None:
            return self._values
        else:
            return self._values[valuePos]


    def showNames(self, valuePos=None):
        if valuePos == None:
            return self._keys
        else:
            return self._keys[valuePos]


    def returnIndexofName(self, name:str):
        return self._keys.index(name)


    def showLength(self):
        return self._length
    

    def updatePositions(self, currentResolution):
        
        for names in self.dictionary:
            posX = self.dictionary[names][0]
            posY = self.dictionary[names][1]
            newPosX = posX
            newPosY = posY
            self.dictionary[names] = (newPosX, newPosY)

        for i in self._dictionary:
            print(i)
        
        # self._values = tuple(self._dictionary.values())
        # self._keys = tuple(self._dictionary.keys())
        # self._length = len(self._values)
            
    
    def updateLanguage(self, dict):
        pass