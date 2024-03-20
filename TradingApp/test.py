#from yahoo_fin.stock_info import *
#print(get_data('HDFCBANK.NS'))


import yahoo_fin.stock_info as si
	
quote = si.get_quote_table("HDFCBANK.NS")
print(quote)





'''import sqlite3 as db

# Specify the path to your SQLite database file
conn = db.connect('datastore.db')
cursor = conn.cursor()

# Execute a SELECT query to fetch all rows from a table (replace 'your_table_name' with the actual table name)
cursor.execute('SELECT * FROM Stocks')

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the fetched data
for row in rows:
    print(row)

# Don't forget to close the connection when you're done
conn.close()
'''