from connect import get_connection

def get_all_todos(db_name, table_name):
	try:
		cursor, db_connection = get_connection(db_name)
		query = """SELECT * FROM {}""".format(table_name)
		cursor.execute(query)
		results = cursor.fetchall()
		for result in results:
			print(result)
		cursor.close()

	except Exception as e:
		print(e)

	finally:
		if db_connection:
			db_connection.close()
			print("Connection closed")


get_all_todos('todos', 'todo')