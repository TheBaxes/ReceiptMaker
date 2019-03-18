from item_type_dao import ItemTypeDAO
from db import DBHandler
from item_type import ItemType

class ItemTypeDAOImpl(ItemTypeDAO):
    def __init__(self):
        self.db = DBHandler.getInstance()

    def getAllItemTypes(self):
        result = self.db.fetchAllExecution("SELECT * FROM item_types")
        return [ItemType(*row) for row in result]

    def getItemType(self, itid):
        row = self.db.fetchOneExecution("SELECT * FROM item_types WHERE id = ?",
                                        (itid,))
        return ItemType(*row)

    def insertItemType(self, item_type):
        self.db.commitExecution("INSERT INTO item_types(description) VALUES(?)",
                                (item_type.desc,))
    
    def updateItemType(self, item_type):
        self.db.commitExecution("UPDATE item_types SET description = ?"
                                " WHERE id = ?", (item_type.desc, item_type.itid))

    def deleteItemType(self, item_type):
        self.db.commitExecution("DELETE FROM item_types WHERE id = ?", (item_type.itid,))
