from client_dao_impl import ClientDAOImpl
from invoice import Invoice

class InvoiceFactory(object):
    def __init__(self):
        self.client_dao = ClientDAOImpl()
    
    def getInvoice(self, rid, client, invoice_state = "unpaid", invoice_date = None):
        client = self.client_dao.getClient(client)
        return Invoice(rid, client, invoice_state, invoice_date)
