import sqlite3
conn=sqlite3.connect(r'/home/justanotherlad/Desktop/bill_db.db')
print("Database created/ OPENED Successfully")

conn.execute("CREATE TABLE ELECTRICITY_BILL(SWASTIKRITAM REAL, NEELDHRITI REAL, DEEP REAL)")
print("Table CREATED Successfully")

conn.execute("INSERT INTO ELECTRICITY_BILL(SWASTIKRITAM,NEELDHRITI,DEEP) VALUES(1008,841,1215)")


conn.commit()
conn.close()
