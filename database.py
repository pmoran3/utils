"""Docstring.
 """

from __future__ import print_function
import fs, sqlite3, datetime
import MySQLdb

def connect_to_mysql(host, username, password, db_name):
  """Return a MySQL database connection. """
  return MySQLdb.connect(host, username, password, db_name)

def connect_to_sqlite(host, db_name):
  """Return an sqlite database connection. """
  return sqlite3.connect(host + db_name)

def load_database_credentials(cred_file):
  """Read a file with database username and password and 
  return a tuple. """
  with open(cred_file, 'r') as creds:

    # Ensure the file contents are on one line
    login = creds.read().replace('\n', ' ').split() 

    if len(login) < 2:
      raise ValueError(("Credential file must contain username and password,"
                        " separated by a space and nothing else."))
      
    return (login[0], login[1])

def get_database_connection():
  """Authenticate to the database as done in the db_write and db_grab
  functions.  Returns an active database connection, this must be closed 
  by the user. """

  # Configure for MySQL 
  if fs.use_mysql: 
    db_connection = connect_to_mysql(fs.MySQL_DB_path, fs.mysql_uname, 
                                     fs.mysql_psswrd, "CLAS12OCR")
  # Configure for sqlite 
  else:
    db_connection = connect_to_sqlite(fs.SQLite_DB_path, fs.DB_name)

  # Create a cursor object for executing statements. 
  sql = db_connection.cursor() 

  # For SQLite, foreign keys need to be enabled
  # manually. 
  if not fs.use_mysql:
    sql.execute("PRAGMA foreign_keys = ON;")
    
  return db_connection, sql 

def get_users(sql):
  """Get a set of database users from the Users table. """
  
  query = """
  SELECT DISTINCT User FROM Users
  """
  sql.execute(query)

  # The result of fetchall is a list of tuples, we need
  # just the first element of each tuple. 
  return { user_tuple[0] for user_tuple in sql.fetchall() }