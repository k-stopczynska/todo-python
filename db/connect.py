import mysql.connector
import logging
from db.utils import get_db_credentials


user, password, host = get_db_credentials()


def connect_db(db_name):
	try:
		db_connection = mysql.connector.connect(
			host=host, user=user, password=password, database=db_name
		)
		return db_connection
	except mysql.connector.Error as e:
		print(f"Error connecting to MySQL database: {e}")
		raise e
	except ValueError as e:
		print(f"ValueError: {e}")
		raise e
	except Exception as e:
		logging.exception(f"Unexpected error occurred: {e}")
		raise e


def get_connection(db_name):
	db_connection = connect_db(db_name)
	cursor = db_connection.cursor()
	return cursor, db_connection


