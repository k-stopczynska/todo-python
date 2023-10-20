from db.connect import get_connection
from db.utils import map_tuple_to_dict


def get_todos_by_status(db_name, table_name, status):
	try:
		cursor, db_connection = get_connection(db_name)
		query = """SELECT * FROM {} as t WHERE t.status = '{}'""".format(table_name, status)
		print(query)
		cursor.execute(query)
		results = cursor.fetchall()
		todos = map_tuple_to_dict(results)
		cursor.close()

	except Exception as e:
		print(e)

	finally:
		if db_connection:
			db_connection.close()
			print("Connection closed")
	return todos

get_todos_by_status('todos', 'todo', 'done')