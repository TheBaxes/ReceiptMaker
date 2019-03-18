class ItemTypeDAO(object):
    def getAllItemTypes(self):
        raise NotImplementedError

    def getItemType(self, itid):
        raise NotImplementedError

    def insertItemType(self, item_type):
        raise NotImplementedError
    
    def updateItemType(self, item_type):
        raise NotImplementedError

    def deleteItemType(self, item_type):
        raise NotImplementedError
