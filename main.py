from pprint import pprint
from cmd import Cmd
from client_dao_impl import ClientDAOImpl
from item_type_dao_impl import ItemTypeDAOImpl
from item_dao_impl import ItemDAOImpl
from invoice_dao_impl import InvoiceDAOImpl
from client import Client
from item_type import ItemType
from item_factory import ItemFactory
from invoice_factory import InvoiceFactory

class Promt(Cmd):
    def __init__(self):
        super(Promt, self).__init__()
        self.client_dao = ClientDAOImpl()
        self.item_type_dao = ItemTypeDAOImpl()
        self.item_dao = ItemDAOImpl()
        self.invoice_dao = InvoiceDAOImpl()
        self.current_invoice = None
        self.invoice_factory = InvoiceFactory()
        self.item_factory = ItemFactory()
        
    def do_EOF(self, inp):
        ''' EXIT '''
        print()
        return True
        
    def do_create_client(self, inp):
        ''' Create a client with the following format:
            name last_name gender birth_date(YYYY-MM-DD) marital_status'''
        args = inp.split(" ")
        if len(args) < 5:
            print("Wrong args")
        else:
            client = Client(None, *args)
            self.client_dao.insertClient(client)

    def do_modify_client(self, inp):
        ''' Modify a client with the following syntax:
            id attr new_value '''
        args = inp.split(" ")
        if len(args) < 3:
            print("Wrong args")
        else:
            client = self.client_dao.getClient(args[0])
            setattr(client, args[1], args[2])
            self.client_dao.updateClient(client)

    def do_delete_client(self, inp):
        ''' Delete a client using its id '''
        client = self.client_dao.getClient(inp)
        self.client_dao.deleteClient(client)

    def do_show_client(self, inp):
        ''' Show a client's info '''
        print(self.client_dao.getClient(inp))
        
    def do_show_all_clients(self, inp):
        ''' Prints all clients '''
        for row in self.client_dao.getAllClients():
            pprint(row)

    def do_create_item_type(self, inp):
        ''' Create item type '''
        item_type = ItemType(None, inp)
        self.item_type_dao.insertItemType(item_type)

    def do_modify_item_type(self, inp):
        ''' Modify an item type with the following syntax:
            id attr new_value '''
        args = inp.split(" ")
        if len(args) < 3:
            print("Wrong args")
        else:
            item_type = self.item_type_dao.getItemType(args[0])
            setattr(item_type, args[1], args[2])
            self.item_type_dao.updateItemType(item_type)

    def do_delete_item_type(self, inp):
        ''' Delete an item type using its id '''
        item_type = self.item_type_dao.getItemType(inp)
        self.item_type_dao.deleteItemType(item_type)

    def do_show_item_type(self, inp):
        ''' Show an item type's info '''
        print(self.item_type_dao.getItemType(inp))

    def do_show_all_item_types(self, inp):
        ''' Prints all item types '''
        for row in self.item_type_dao.getAllItemTypes():
            pprint(row)

    def do_create_item(self, inp):
        ''' Create item type with the following format:
            item_type_id description value_per_unit'''
        args = inp.split(" ")
        if len(args) < 3:
            print("Wrong args amount")
        else:
            item = self.item_factory.getItem(None, *args)
            self.item_dao.insertItem(item)

    def do_modify_item(self, inp):
        ''' Modify an item with the following syntax:
            id attr new_value '''
        args = inp.split(" ")
        if len(args) < 3:
            print("Wrong args")
        else:
            item = self.item_dao.getItem(args[0])
            setattr(item, args[1], args[2])
            self.item_dao.updateItem(item)

    def do_delete_item(self, inp):
        ''' Delete an item using its id '''
        item = self.item_dao.getItem(inp)
        self.item_dao.deleteItem(item)

    def do_show_item(self, inp):
        ''' Show an item's info '''
        print(self.item_dao.getItem(inp))
            
    def do_show_all_items(self, inp):
        ''' Prints all clients '''
        for row in self.item_dao.getAllItems():
            print(repr(row))

    def do_create_invoice(self, inp):
        ''' Create and modify a invoice for a client_id'''
        invoice = self.invoice_factory.getInvoice(None, inp)
        current_invoice = self.invoice_dao.insertInvoice(invoice)
        self.current_invoice = self.invoice_dao.getInvoice(current_invoice)

    def do_change_current_invoice(self, inp):
        ''' Change current invoice using its id '''
        self.current_invoice = self.invoice_dao.getInvoice(inp)
        
    def do_modify_invoice(self, inp):
        ''' Modify the current invoice header with the following syntax:
            id attr new_value '''
        args = inp.split(" ")
        if len(args) < 3:
            print("Wrong args")
        else:
            setattr(self.current_invoice, args[1], args[2])
            self.invoice_dao.updateInvoice(self.current_invoice)
        
    def do_show_current_invoice_header(self, inp):
        ''' Prints current invoice header '''
        pprint(self.invoice_dao.getInvoice(self.current_invoice.rid))

    def do_delete_invoice(self, inp):
        ''' Delete an invoice using its id '''
        invoice = self.invoice_dao.getInvoice(inp)
        self.invoice_dao.deleteInvoice(invoice)

    def do_show_all_invoices_headers(self, inp):
        ''' Show all invoices info '''
        pprint(self.invoice_dao.getAllInvoices())
        
    def do_add_item(self, inp):
        ''' Add an item to the current invoice '''
        item = self.item_dao.getItem(inp)
        self.invoice_dao.insertItemToInvoice(self.current_invoice, item)

    def do_show_items(self, inp):
        ''' Show all items associated to the current invoice '''
        pprint(self.invoice_dao.getInvoiceItems(self.current_invoice.rid))

    def do_remove_item(self, inp):
        ''' Remove an item from the current invoice '''
        item = self.item_dao.getItem(inp)
        self.invoice_dao.deteleItemFromInvoice(self.current_invoice, item)

    def do_print_report(self, inp):
        ''' Print the current invoice information '''
        self.do_show_current_invoice_header("")
        items = self.invoice_dao.getInvoiceItems(self.current_invoice.rid)
        total = 0
        for item in items:
            total += item.val_unit
        print("total cost: " + str(total))
        print("items: ")
        self.do_show_items("")
        
Promt().cmdloop()
             
# from db import DBHandler
# from client_dao_impl import ClientDAOImpl


# db = DBHandler.getInstance()
# db.commitExecution("INSERT INTO clients(name, last_name, gender, birth_date, marital_status)"
#                    "VALUES(?, ?, ?, ?, ?)", ('JUAN', 'PEREZ', 'MALE', '2010-10-10', 'SINGLE'))

# db.commitExecution("INSERT INTO clients(name, last_name, gender, birth_date, marital_status)"
#                    "VALUES(?, ?, ?, ?, ?)", ('JUAN', 'PEREZ', 'MALE', '2010-10-10', 'SINGLE'))

# dao = ClientDAOImpl()
# for row in dao.getAllClients():
#     pprint(vars(row))

# c = dao.getClient(1)
# pprint(vars(c))

# c.name = "PEPE"
# dao.updateClient(c)
# pprint(vars(dao.getClient(1)))

# print()

# dao.deleteClient(c)
# for row in dao.getAllClients():
#     pprint(vars(row))
