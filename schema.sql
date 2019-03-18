CREATE TABLE IF NOT EXISTS clients (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       last_name TEXT NOT NULL,
       gender TEXT NOT NULL,
       birth_date DATE NOT NULL,
       marital_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS item_types (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS items (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       item_type_id INTEGER NOT NULL,
       description TEXT NOT NULL,
       value_per_unit DOUBLE NOT NULL,
       FOREIGN KEY (item_type_id) REFERENCES item_type (id)
);

CREATE TABLE IF NOT EXISTS invoices (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       client_id INTEGER NOT NULL,
       invoice_state TEXT NOT NULL,
       invoice_date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
       FOREIGN KEY (client_id) REFERENCES clients (id)
);

CREATE TABLE IF NOT EXISTS invoices_items (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       invoice_id INTEGER NOT NULL,
       item_id INTEGER NOT NULL,
       FOREIGN KEY (invoice_id) REFERENCES invoices (id),
       FOREIGN KEY (item_id) REFERENCES items (id)
);
