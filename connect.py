import mysql.connector
import logging
from utils import get_db_credentials


user, password, host = get_db_credentials()
db_name = 'todo_list'


def connect_db(db_name):
	try:
		db_connection = mysql.connector.connect(
			host, user, password, database=db_name
		)
		return db_connection
	except mysql.connector.Error as e:
		print(f"Error connecting to MySQL database: {e}")
		raise e
	except ValueError as e:
		print(f"ValueError: {e}")
		raise e
	except Exception as e:
		# Catch unexpected exceptions, log them, and raise to crash the program
		logging.exception(f"Unexpected error occurred: {e}")
		raise e


