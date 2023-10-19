from create_db import create_and_use_db
from connect import get_connection


def create_table():
	try:
		db_name = 'todos'
		cursor, db_connection = get_connection(db_name)
		create_and_use_db(db_name)
		query = """CREATE TABLE todo (todo_id INT PRIMARY KEY AUTO_INCREMENT, 
		title VARCHAR(35) NOT NULL, description VARCHAR(255) NOT NULL, status 
		ENUM('todo', 'pending', 'done'), deadline DATE NOT NULL)"""
		cursor.execute(query)
	except Exception as e:
		print(e)
	finally:
		if db_connection:
			db_connection.close()
			print("Connection closed")
