class InvoiceDAO(object):
    def getAllInvoices(self):
        raise NotImplementedError

    def getInvoice(self, rid):
        raise NotImplementedError

    def getInvoiceItems(self, rid):
        raise NotImplementedError

    def insertInvoice(self, invoice):
        raise NotImplementedError

    def insertItemToInvoice(self, invoice, item):
        raise NotImplementedError
    
    def updateInvoice(self, invoice):
        raise NotImplementedError

    def deleteInvoice(self, invoice):
        raise NotImplementedError

    def deleteItemFromInvoice(self, invoice, item):
        raise NotImplementedError
