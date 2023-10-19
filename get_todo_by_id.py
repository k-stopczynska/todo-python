from connect import get_connection


def get_todo_by_id(db_name, table_name, todo_id):
	try:
		cursor, db_connection = get_connection(db_name)
		query = """SELECT * FROM {} as t WHERE t.todo_id = {}""".format(table_name, todo_id)
		cursor.execute(query)
		results = cursor.fetchall()
		cursor.close()
	except Exception as e:
		print(e)

	finally:
		if db_connection:
			db_connection.close()
			print("Connection closed")


get_todo_by_id('todos', 'todo', 1)