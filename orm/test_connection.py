import sqlite3

create_contacts_query = """
  CREATE TABLE IF NOT EXISTS contacts(
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
"""
add_contact = """
  insert into contacts(first_name, last_name, email, phone)
  values
  ("john", "doe", "john_doe@gmail.com", "123-555-6677")
"""

get_contacts_query = """select * from contacts;"""

con = sqlite3.connect("orm.db")
cur = con.cursor()
create_response = cur.execute(create_contacts_query)
print(create_response)
add_response = cur.execute(add_contact)
print(add_response)
select_response = cur.execute(get_contacts_query)
print(select_response)
john = select_response.fetchone()
print(type(john))
print(john)
