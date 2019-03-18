class ItemDAO(object):
    def getAllItems(self):
        raise NotImplementedError

    def getItem(self, iid):
        raise NotImplementedError

    def insertItem(self, item):
        raise NotImplementedError
    
    def updateItem(self, item):
        raise NotImplementedError

    def deleteItem(self, item):
        raise NotImplementedError
