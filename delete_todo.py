from connect import get_connection


def delete_todo(db_name, table_name, todo_id):
	try:
		cursor, db_connection = get_connection(db_name)
		query = """DELETE FROM {} as t WHERE t.todo_id = {}""".format(table_name, todo_id)
		print(query)
		cursor.execute(query)
		db_connection.commit()
		cursor.close()
	except Exception as e:
		print(e)

	finally:
		if db_connection:
			db_connection.close()
			print("Connection closed")


delete_todo('todos', 'todo', 3)