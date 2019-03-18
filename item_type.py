class ItemType(object):
    def __init__(self, itid, desc):
        self.__itid = itid
        self.__desc = desc

    def __repr__(self):
        return "id: " + repr(self.__itid) + " desc: " + repr(self.__desc)
        
    @property
    def itid(self):
        return self.__itid

    @itid.setter
    def itid(self, itid):
        self.__itid = itid

    @property
    def desc(self):
        return self.__desc

    @desc.setter
    def desc(self, desc):
        self.__desc = desc
