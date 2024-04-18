import pyodbc

# Connection parameters

driver = '{ODBC Driver 18 for SQL Server}'

server = 'localhost'

database = 'CrazyCleanCarptes'

username = 'sa'

password = 'reallyStrongPwd123'

# Establish connection

conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=No')

# Create a cursor

cursor = conn.cursor()

# Prepare and execute the UPDATE query with parameters

query = "UPDATE Card SET card_lname = ?"

cursor.execute(query, ('GABE'))

# Commit the transaction

conn.commit()

# Close cursor and connection

cursor.close()

conn.close()

