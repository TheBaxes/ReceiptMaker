from item_type_dao_impl import ItemTypeDAOImpl
from item import Item

class ItemFactory(object):
    def __init__(self):
        self.item_type_dao = ItemTypeDAOImpl()
    
    def getItem(self, iid, item_type, desc, val_unit):
        item_type = self.item_type_dao.getItemType(item_type)
        return Item(iid, item_type, desc, val_unit)
