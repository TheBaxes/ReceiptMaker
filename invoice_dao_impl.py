from invoice_dao import InvoiceDAO
from db import DBHandler
from invoice import Invoice
from item_dao_impl import ItemDAOImpl
from invoice_factory import InvoiceFactory

class InvoiceDAOImpl(InvoiceDAO):
    def __init__(self):
        self.db = DBHandler.getInstance()
        self.invoice_factory = InvoiceFactory()
        self.item_dao = ItemDAOImpl()

    def getAllInvoices(self):
        result = self.db.fetchAllExecution("SELECT * FROM invoices")
        return [self.invoice_factory.getInvoice(*row) for row in result]

    def getInvoice(self, rid):
        row = self.db.fetchOneExecution("SELECT * FROM invoices WHERE id = ?",
                                        (rid,))
        return self.invoice_factory.getInvoice(*row)

    def getInvoiceItems(self, rid):
        rows = self.db.fetchAllExecution("SELECT item_id from invoices_items where invoice_id = ? ", (rid,))
        items = []
        for row in rows:
            items.append(self.item_dao.getItem(row[0]))
        return items
    
    def insertInvoice(self, invoice):
        return self.db.commitExecution("INSERT INTO invoices(client_id, invoice_state) VALUES(?, ?)",
                                        (invoice.client.cid, invoice.invoice_state))

    def insertItemToInvoice(self, invoice, item):
        self.db.commitExecution("INSERT INTO invoices_items(invoice_id, item_id) "
                                "VALUES(?, ?)", (invoice.rid, item.iid))
        
    def updateInvoice(self, invoice):
        self.db.commitExecution("UPDATE invoices SET client_id = ?, invoice_state = ?"
                                " WHERE id = ?", (invoice.client.cid, invoice.invoice_state))

    def deleteInvoice(self, invoice):
        self.db.commitExecution("DELETE FROM invoices_items WHERE invoice_id = ?", (invoice.rid,))
        self.db.commitExecution("DELETE FROM invoices WHERE id = ?", (invoice.rid,))

    def deleteItemFromInvoice(self, invoice, item):
        self.db.commitExecution("DELETE TOP 1 FROM invoices_items WHERE invoice_id = ?, "
                                "item_id = ?", (invoice.rid, item.iid))
