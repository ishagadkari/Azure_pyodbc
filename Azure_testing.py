import pyodbc

# Establishing the string for connection, required parameters: server, database, username, and password.
def establish_string(server, database, username, password):
    string_established = f"Driver=ODBC Driver 18 for SQL Server;Server={server};Database={database};Uid={username};Pwd={password};"
    return string_established

# Establishing the connection using pyodbc.connect() method.
def establish_connection(string_established):
    try:
        connection = pyodbc.connect(string_established)
        return connection
    except pyodbc.Error as e:
        print(f"Error establishing connection: {e}")
        return None

# Creating cursor
def create_cursor(connection):
    cursor = connection.cursor()
    return cursor

# Adding a table by opening the file path, and reading it into a query.
# Using cursor.execute() function.
def adding_table(query_file_path, cursor, connection):
    try:
        with open(query_file_path, 'r') as file:
            query = file.read()

        cursor.execute(query)
        connection.commit()
    except pyodbc.Error as e:
        print(f"Error executing query: {e}")

'''
def table(table_name, columns, cursor, connection):
    try:
        create_table_query = f"CREATE TABLE {table_name} ("
        for column_name, data_type in columns:
            create_table_query += f"[{column_name}] {data_type}, "
        create_table_query = create_table_query.rstrip(', ')
        create_table_query += ")"
        cursor.execute(create_table_query)
        connection.commit()
    except pyodbc.Error as e:
        print(f"Error executing query: {e}")
'''

# Adds rows to the table. This method recognizes which table the rows should be added to by
# the table_name. 'rows' is a list of tuples, each tuple specifies a row in the table.
def adding_rows(table_name, rows, cursor, connection):
    try:
        insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(rows[0]))})"
        for row in rows:
            cursor.execute(insert_query, row)

        # Commit the changes
        connection.commit()
    except pyodbc.Error as e:
        print(f"Error adding rows to the table: {e}")

# Closing the cursor and the connection.
def close_connection(cursor, connection):
    # Close the cursor
    cursor.close()
    # Close the connection
    connection.close()

if __name__ == "__main__":
    es = establish_string("ishasandbox1.database.windows.net", "ishaSandbox", "isha.gadkari", "Bhopal123456")
    connection = establish_connection(es)
    cursor = create_cursor(connection)
    #adding_table("C:\\Users\\ishag\\Documents\\Azure_testing\\Query2.sql", cursor, connection)
    #columns = [('ID', 'INT'), ('Name', 'VARCHAR(255)'), ('Age', 'INT')]
    #table("new_table", columns, cursor, connection)
    rows_to_insert = [('J', 30, 1), ('A', 25, 1)]
    adding_rows("Table2", rows_to_insert, cursor, connection)
    close_connection(cursor, connection)
