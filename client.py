from datetime import date

class Client(object):    
    def __init__(self, cid, name, last_name, gender, birth_date, marital_status):
        self.__cid = cid
        self.__name = name
        self.__last_name = last_name
        self.__gender = gender
        self.__birth_date = birth_date
        self.__marital_status = marital_status

    def __repr__(self):
        return ("id: " + repr(self.__cid) + " name: " + repr(self.__name)) + " last_name: " + \
            repr(self.__last_name) + " gender: " + repr(self.__gender) + " birth_date: " + \
            self.__birth_date.isoformat() + " marital_status: " + repr(self.__marital_status)
        
    @property
    def cid(self):
        return self.__cid

    @cid.setter
    def cid(self, cid):
        self.__cid = cid

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        self.__birth_date = birth_date

    @property
    def marital_status(self):
        return self.__marital_status

    @marital_status.setter
    def marital_status(self, marital_status):
        self.__marital_status = marital_status
