from db.connect import get_connection


def get_todos_by_status(db_name, table_name, status):
	try:
		cursor, db_connection = get_connection(db_name)
		query = """SELECT * FROM {} as t WHERE t.status = '{}'""".format(table_name, status)
		print(query)
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


get_todos_by_status('todos', 'todo', 'done')