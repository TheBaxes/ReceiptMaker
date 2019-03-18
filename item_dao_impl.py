from item_dao import ItemDAO
from db import DBHandler
from item_factory import ItemFactory

class ItemDAOImpl(ItemDAO):
    def __init__(self):
        self.db = DBHandler.getInstance()
        self.item_factory = ItemFactory()
        
    def getAllItems(self):
        result = self.db.fetchAllExecution("SELECT * FROM items")
        return [self.item_factory.getItem(*row) for row in result]

    def getItem(self, iid):
        row = self.db.fetchOneExecution("SELECT * FROM items WHERE id = ?",
                                        (iid,))
        return self.item_factory.getItem(*row)

    def insertItem(self, item):
        self.db.commitExecution("INSERT INTO items(item_type_id, description, value_per_unit) "
                                "VALUES(?, ?, ?)", (item.item_type.itid, item.desc, item.val_unit))
    
    def updateItem(self, item):
        self.db.commitExecution("UPDATE items SET item_type_id = ?, description = ?"
                                "value_per_unit = ? WHERE id = ?",
                                (item.item_type.itid, item.desc, item.val_unit,
                                 item_type.iid))

    def deleteItem(self, item):
        self.db.commitExecution("DELETE FROM items WHERE id = ?", (item.tid,))
