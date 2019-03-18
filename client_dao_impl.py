from client_dao import ClientDAO
from db import DBHandler
from client import Client

class ClientDAOImpl(ClientDAO):
    def __init__(self):
        self.db = DBHandler.getInstance()

    def getAllClients(self):
        result = self.db.fetchAllExecution("SELECT * FROM clients")
        return [Client(*row) for row in result]

    def getClient(self, cid):
        row = self.db.fetchOneExecution("SELECT * FROM clients WHERE id = ?",
                                        (cid,))
        return Client(*row)

    def insertClient(self, client):
        self.db.commitExecution("INSERT INTO clients(name, last_name, gender, birth_date, marital_status)"
                                "VALUES(?, ?, ?, ?, ?)", (client.name, client.last_name, client.gender,
                                                          client.birth_date, client.marital_status))
    
    def updateClient(self, client):
        self.db.commitExecution("UPDATE clients SET name = ?, last_name = ?, "
                                "gender = ?, birth_date = ?, marital_status = ?"
                                " WHERE id = ?", (client.name, client.last_name,
                                                client.gender, client.birth_date,
                                                client.marital_status, client.cid))

    def deleteClient(self, client):
        self.db.commitExecution("DELETE FROM clients WHERE id = ?", (client.cid,))
