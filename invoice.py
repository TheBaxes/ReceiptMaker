class Invoice(object):
    def __init__(self, rid, client, invoice_state = "unpaid", invoice_date = None):
        self.__rid = rid
        self.__client = client
        self.__invoice_state = invoice_state
        self.__invoice_date = invoice_date

    def __repr__(self):
        return "id: " + repr(self.__rid) + " client: (" + repr(self.__client) + \
            ") invoice_state: " + repr(self.__invoice_state) + " invoice_date:" + \
            repr(self.__invoice_date)

    @property
    def rid(self):
        return self.__rid

    @rid.setter
    def rid(self, rid):
        self.__rid = rid

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, client):
        self.__client = client

    @property
    def invoice_state(self):
        return self.__invoice_state

    @invoice_state.setter
    def invoice_state(self, invoice_state):
        self.__invoice_state = invoice_state
