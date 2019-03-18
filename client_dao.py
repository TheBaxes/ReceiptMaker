class ClientDAO(object):
    def getAllClients(self):
        raise NotImplementedError

    def getClient(self, cid):
        raise NotImplementedError

    def insertClient(self, client):
        raise NotImplementedError
    
    def updateClient(self, client):
        raise NotImplementedError

    def deleteClient(self, client):
        raise NotImplementedError
