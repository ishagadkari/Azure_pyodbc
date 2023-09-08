import pyodbc

#establishing the string for connection, required parameters: server, database, username, and password.
def establish_string(server, database, username, password):
    string_established = f"Driver=ODBC Driver 18 for SQL Server;Server={server};Database={database};Uid={username};Pwd={password};"
    return string_established

#establishing the connection using pyodbc.connect() method.
def establish_connection(string_established):
    try:
        connection = pyodbc.connect(string_established)
        return connection
    except pyodbc.Error as e:
        print(f"Error establishing connection: {e}")
        return None

#creating cursor
def create_cursor(connection):
    cursor = connection.cursor()
    return cursor

#adding table by opening the file path, and reading it in a query.
#using cursor.execute() function.
def adding_table(query_file_path, cursor, connection):
    try:
        with open(query_file_path, 'r') as file:
            query = file.read()

        cursor.execute(query)
        connection.commit()
    except pyodbc.Error as e:
        print(f"Error executing query: {e}")

#closing the cursor and the connection. 
def close_connection(cursor, connection):
    # Close the cursor
     cursor.close()
     # Close the connection
     connection.close()


if __name__ == "__main__":

    es = establish_string("ishasandbox1.database.windows.net", "ishaSandbox", "isha.gadkari", "Bhopal123456")
    connection = establish_connection(es)
    cursor = create_cursor(connection)
    adding_table("C:\\Users\\ishag\\Documents\\Azure_testing\\Query2.sql", cursor, connection)
    close_connection(cursor, connection)
