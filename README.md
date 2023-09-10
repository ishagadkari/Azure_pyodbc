## PyODBC SQL Database Interaction

This Python script provides functions for interacting with a SQL database using the `pyodbc` library. It includes functions for establishing a database connection, creating a cursor, adding tables, and inserting rows into existing tables.

### Prerequisites

    
   PyODBC library (pip install pyodbc)
   SQL Server credentials (server, database, username, password)

  ### Usage

  1. Import PyODBC and Required Libraries
     ```bash
       pip install pyodbc
     ```

  3. Establish a Database Connection
     Modify the establish_string function to specify your SQL Server's connection details, including server name, database name, username, and password.
     ```
      es = establish_string("your_server_name", "your_database_name", "your_username", "your_password")
      connection = establish_connection(es)
      cursor = create_cursor(connection)
     ```
     
  4. Adding a Table (Optional)
     If you want to create a new table, you can use the adding_table function by specifying the path to a SQL query file that defines the table schema.
     ``` 
     adding_table("path_to_query_file.sql", cursor, connection)
     ```
  5. Adding Rows to an Existing Table
     To add rows to an existing table, use the adding_rows function. Specify the table name and provide a list of tuples, where each tuple represents a row to be inserted.
     ```
     rows_to_insert = [('J', 30, 1), ('A', 25, 1)]
     adding_rows("Table2", rows_to_insert, cursor, connection)
     ```
     
  6. Closing the Connection
     Finally, close the cursor and the database connection when you're done:
     ```
      close_connection(cursor, connection)
     ```


     

