class Item(object):
    def __init__(self, iid, item_type, desc, val_unit):
        self.__iid = iid
        self.__item_type = item_type
        self.__desc = desc
        self.__val_unit = val_unit

    def __repr__(self):
        return "id: " + repr(self.__iid) + " type: (" + repr(self.__item_type) + \
            ") desc: " + repr(self.__desc) + " val per unit: " + repr(self.__val_unit)

    @property
    def iid(self):
        return self.__iid

    @iid.setter
    def iid(self, iid):
        self.__iid = iid

    @property
    def item_type(self):
        return self.__item_type

    @item_type.setter
    def item_type(self, item_type):
        self.__item_type = item_type

    @property
    def desc(self):
        return self.__desc

    @desc.setter
    def desc(self, desc):
        self.__desc = desc

    @property
    def val_unit(self):
        return self.__val_unit

    @val_unit.setter
    def val_unit(self, val_unit):
        self.__val_unit = val_unit
